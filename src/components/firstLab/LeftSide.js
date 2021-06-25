import React, { useState } from 'react'
import "./index.css"
import { Box, ChakraProvider, Container, Button, Heading, VStack, Image, HStack, Tag } from "@chakra-ui/react";
// import Axios from "axios";
// import Upload from "../Upload/Upload";
import axios from 'axios';

const getUrl = 'http://localhost:8080/stats'


const LeftSide = () => {
    const [uploadedImage, setuploadedImage] = useState(null)
    const [imageUrl, setimageUrl] = useState(null)
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
                            <Button
                                colorScheme="blue"
                                size="lg"
                                onClick={() =>
                                    axios.get(getUrl).then((resp) => {
                                        setimageUrl(resp.data.data.imageUrl)
                                        setuploadedImage(1)
                                    })
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
        </div>
    )
}

export default LeftSide
