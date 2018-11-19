get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

import math

def getDistance(v,w):
    v_1, v_2, v_3 = v[0], v[1], v[2]
    w_1, w_2, w_3 = w[0], w[1], w[2]
    
    distance = math.sqrt((v_1**2)*w_1 + (v_2**2)*w_2 + (v_3**2)*w_3)
    
    return distance

def getDistance(v):
    v_1, v_2, v_3 = v[0], v[1], v[2]
    
    distance = math.sqrt(v_1**2 + v_2**2 + v_3**2)
    
    return distance

def RGB_level_to_Gray_level(im):
    m = im.shape[0]
    n = im.shape[1]
    im2 = np.zeros([m, n])
    for i in range (m):
        for j in range (n):
            im2[i,j] = getDistance(im[i,j,:])
    return im2

def Gray_level_To_BW_level(image_gray_level):
    m=image_gray_level.shape[0]
    n=image_gray_level.shape[1]
    im_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if image_gray_level[i,j]>120:
                im_bw[i,j]=1
            else:
                im_bw[i,j]=0
    return im_bw


img = mpimg.imread('image/tree.jpeg')
img = RGB_level_to_Gray_level(img)
arr = np.asarray(img)
plt.imshow(arr, cmap='gray')
plt.show()

img =  Gray_level_To_BW_level(img)
arr = np.asarray(img)
plt.imshow(arr, cmap='gray')
plt.show()

fname = 'image/tree.jpeg'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap='gray')
plt.show()

#plt.imshow(img)
