import matplotlib.pyplot as plt
import numpy as np

def getDistance(v,w):
    v_1, v_2, v_3 = v[0], v[1], v[2]
    w_1, w_2, w_3 = w[0], w[1], w[2]
    
    distance = math.sqrt((v_1**2)*w_1 + (v_2**2)*w_2 + (v_3**2)*w_3)
    
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

image1=plt.imread("deneme.png")
plt.imshow(image1)
plt.show()

image2=convert_rgb_to_gray_level(image1)
plt.imshow(image2,cmap='gray')
plt.show()

image3=convert_rgb_to_BW(image2)
plt.imshow(image3,cmap='gray')
plt.show()

def pixel_compenent(resim):    
    m,n=resim.shape[0],resim.shape[1]
    ext,int=0,0
    for i in range (1,m-1):
        for j in range(1,n-1):
            poi=resim[i:i+2,j:j+2]
	    black,white = 0,0
            for k in range(2):
                for l in range(2):
                    if poi[k][l]==1:black +=1      
                    else: white += 1
                        
            if(black>wihte and white>0) : ext=ext+1
            elif(white>black and black>0): int += 1
                
                
    print(ext)
    print(int)
    

pixel_compenent(image3)
