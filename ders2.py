import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#img_mpimg.imread('test1.jpg')
#%matplotlib inline
import numpy as np

image_1=plt.imread("test.jpg")

plt.imshow(image_1)
plt.show()

def myFunc(image_1):
    print("Dimension of image : ",image_1.ndim,"\n")
    print("Shape value of image : ",image_1.shape)
    print("max value for Red : ",np.max(image_1[:,:,0]))#0 degeri R yi gösterir ve 3.boyut katar.
    print("min value for Red : ",np.max(image_1[:,:,0]))
    print("max value for Green : ",np.max(image_1[:,:,1]))
    print("min value for Green : ",np.max(image_1[:,:,1])) #':' işareti her sütünu ve her satırı taramasını saglar.
    print("max value for Blue : ",np.max(image_1[:,:,2]))
    print("min value for Red : ",np.max(image_1[:,:,2]))
    
myFunct(image_1)
    
image_1[:,:,0] = image_1[:,:,0]+150
plt.imshow(image_1)
plt.show()


def my_function_1(my_img):
    
    print("eksen sayisi : ",my_img.ndim)
    print("eksen degerleri :",my_img.shape)
    
    print("en kucuk kirmizi renk degeri : ",np.min(my_img[:,:,0]))
    print("en kucuk kirmizi renk degeri : ",np.max(my_img[:,:,0]))
    
    print("en kucuk yesil renk degeri : ",np.min(my_img[:,:,1]))
    print("en kucuk yesil renk degeri : ",np.max(my_img[:,:,1]))
    
    print("en kucuk mavi renk degeri : ",np.min(my_img[:,:,2]))
    print("en kucuk mavi renk degeri : ",np.max(my_img[:,:,2]))
    
my_function_1(im_1)
