import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#img_mpimg.imread('test1.jpg')
#%matplotlib inline
import numpy as np

im_1=plt.imread("1.jpg")

plt.imshow(im_1)
plt.show()

def function(image_1):
    print("Resmin boyutu = ",image_1.ndim,"\n") 
    print("Resmin Shape değeri = ",image_1.shape,"\n")
    print("Red için min değer = ",image_1[:,:,0].min(),"\n") #':' hangi yerde kullanıldıysa oranın tamamından bahsediyor örneğin burada tüm satırlar ve sütünlar
    print("Red için max değer = ",image_1[:,:,0].max(),"\n") # şuan kırmızı için olan değerlere bakıyoruz 1 olsa yeşil 2 olursa mavi
    
function(im_1)

im_1[:,:,0]=im_1[:,:,0]+50

plt.imshow(im_1)
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
