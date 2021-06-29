import React, { useState } from 'react'
import "./index.css"
import { Box, ChakraProvider, Container, Button, Heading, VStack, Image, HStack, Tag, Radio, FormControl, RadioGroup, FormHelperText, FormLabel } from "@chakra-ui/react";
// import Axios from "axios";
// import Upload from "../Upload/Upload";
import axios from 'axios';

const getUrl = 'http://localhost:8080/stat'


const LeftSide = () => {
    const [uploadedImage, setuploadedImage] = useState(null)
    const [imageUrl, setimageUrl] = useState(null)
    const [country, setCountry] = useState("Russian Federation")
    const [mode, setMode] = useState("population")
    return (
        <div>
            <ChakraProvider>
                <Box
                    minH="100vh"
                    w="100%"
                    bg="gray.200"
                    display="flex"
                    alignItems="center"
                    justifyContent="center"
                >
                    <Container maxWidth="container.l">
                        <VStack>
                            <Heading>График данных</Heading>
                            <select onChange={e => {
                                setMode(e.target.value)
                            }} >
                                <option>
                                    population
                                    </option>
                                <option>
                                    suicides_no
                                    </option>
                            </select>
                            <input type="text" placeholder="Введите страну на английском" onChange={(e) => { setCountry(e.target.value); console.log(country) }} />

                            <Button
                                colorScheme="blue"
                                size="lg"
                                onClick={() => {
                                    const newString = `${getUrl}/${mode}/${country}`
                                    axios.get(newString).then((resp) => {
                                        setimageUrl(resp.data.message1.imageUrl)
                                        setuploadedImage(1)
                                        console.log(resp.data.message1.imageUrl)
                                    })
                                }

                                }
                            >
                                Загрузить график
                             </Button>

                            {uploadedImage && (
                                <VStack my="4">
                                    <Image
                                        src={imageUrl}
                                        width="300px"
                                        height="300px"
                                        alt={uploadedImage.imageName}
                                    />

                                    <HStack>
                                        <Tag variant="outline" colorScheme="blackAlpha">
                                            ~ {Math.floor(uploadedImage.size / 1024)} Kb
                        </Tag>
                                    </HStack>
                                </VStack>
                            )}
                        </VStack>
                    </Container>
                </Box>

            </ChakraProvider>
        </div >
    )
}

export default LeftSide
