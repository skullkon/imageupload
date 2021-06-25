from io import BytesIO
import base64
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage.filters as filt


def ImageNoiser(img):
    im = Image.open(img)
    image_box = im
    images_resized = [[]]
    height = 224
    width = 224
    images_resized = np.array(image_box.resize((height, width)))/255.0
    images_resized = np.array(images_resized)
    image_copy = images_resized.copy()
    fig_ = plt.figure(figsize=(5, 5))
    viewer_3 = fig_.add_subplot(1, 1, 1)
    image_rand = image_copy + (np.random.rand(*image_copy.shape)-0.5)*0.3
    image_rand = (image_rand-image_rand.min()) / \
        (image_rand.max() - image_rand.min())
    image_rand = image_rand.transpose(2, 0, 1)
    image_filt = np.array(
        [filt.gaussian_filter(image_rand[i], 1) for i in range(3)])
    image_filt = image_filt.transpose((1, 2, 0))
    image_rand = image_rand.transpose((1, 2, 0))
    viewer_3.imshow(image_rand)
    fig_.savefig("hello.png")
    return fig_
