package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"mime/multipart"
	"net/http"
	"os"
	"path/filepath"
	"time"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
)

type Base struct {
	Hello string `json:"size"`
}

func main() {
	router := gin.Default()
	router.Use(cors.Default())
	router.POST("/upload", saveFileHandler)
	router.GET("/stats", getStats)
	router.Static("/image", "./image")
	router.Run(":8080")
}

func saveFileHandler(c *gin.Context) {
	file, err := c.FormFile("image")

	if err != nil {
		c.AbortWithStatusJSON(http.StatusBadRequest, gin.H{
			"message": "No file is received",
		})
		return
	}
	extension := filepath.Ext(file.Filename)
	newFileName := uuid.New().String() + extension
	if err := c.SaveUploadedFile(file, "./image/"+newFileName); err != nil {
		log.Println(err)
		c.AbortWithStatusJSON(http.StatusInternalServerError, gin.H{
			"message": "Unable to save the file",
		})
		return
	}
	imageUrl := fmt.Sprintf("http://localhost:8080/image/%s", newFileName)

	client := &http.Client{
		Timeout: time.Second * 10,
	}

	body := &bytes.Buffer{}
	writer := multipart.NewWriter(body)
	fw, _ := writer.CreateFormFile("image", "./image/"+newFileName)
	mile, _ := os.Open("./image/" + newFileName)

	_, _ = io.Copy(fw, mile)
	writer.Close()
	req, _ := http.NewRequest("POST", "http://localhost:5000/image", bytes.NewReader(body.Bytes()))

	req.Header.Set("Content-Type", writer.FormDataContentType())
	rsp, _ := client.Do(req)
	if rsp.StatusCode != http.StatusOK {
		log.Printf("Request failed with response code: %d", rsp.StatusCode)
	}
	base := Base{}
	_ = json.NewDecoder(rsp.Body).Decode(&base)

	ddd, _ := base64.StdEncoding.DecodeString(base.Hello[2:])
	_ = ioutil.WriteFile("./image/"+newFileName, ddd, 0666)

	data := map[string]interface{}{

		"imageName": file,
		"imageUrl":  imageUrl,
		"header":    file.Header,
		"size":      file.Size,
	}
	// log.Println(f)
	c.JSON(200, gin.H{
		"status": 201, "message": "Your file has been successfully uploaded.", "data": data, "final": base.Hello})
}

func getStats(c *gin.Context) {
	newFileName := uuid.New().String() + ".jpg"
	req, _ := http.Get("http://localhost:5000/ai")
	base := Base{}
	_ = json.NewDecoder(req.Body).Decode(&base)
	// log.Println(base.Hello)
	ddd, _ := base64.StdEncoding.DecodeString(base.Hello[2:])
	_ = ioutil.WriteFile("./image/"+newFileName, ddd, 0666)

	imageUrl := fmt.Sprintf("http://localhost:8080/image/%s", newFileName)
	data := map[string]interface{}{
		"imageUrl": imageUrl,
	}
	c.JSON(200, gin.H{
		"status": 201, "message": "Your file has been successfully uploaded.", "data": data})
}
