coding: utf-8
In[31]:
import numpy as np

In[32]:
mask_0=np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)
mask_0/9

In[33]:
mask_1=np.random.randint(20,size=9).reshape(3,3)
mask_2=np.random.randint(5,size=9).reshape(3,3)
print(mask_1)
print("-----------------")
print(mask_2)
print("-----------------")
print(mask_1*mask_2)

In[34]:
sum(sum(mask_1*mask_0))

In[35]:
def get_default_mask_for_mean():
return np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)/9
def apply_mask(part_of_image):
mask= get_default_mask_for_mean()
return sum(sum(part_of_image*mask))

In[36]:
import matplotlib.pyplot as plt

In[40]:
def get_mean_filter(im_1):
#im_1=plt.imread('')
m=im_1.shape[0]
n=im_1.shape[1]
im_2=np.zeros((m,n))
for i in range(1,m-1):
for j in range(1,n-1):
poi= im_1[i-1:i+2,j-1:j+2]
#poi.shape
#input("asasd")
im_2[i,j]=get_median(poi)
#im_2[i,j]=apply_mask(poi)
return im_2

In[41]:
im_4 = get_mean_filter(im_2)

In[38]:
mask_1=np.random.randint(20,size=9).reshape(3,3)
mask_1

In[24]:
mask_1[:,0:1]

In[ ]:
def convert_rgb_to_gray_level(im_1):
m = im.shape[0]
n = im.shape[1]
im2 = np.zeros([m, n])
for i in range (m):
for j in range (n):
im2[i,j] = getDistance(im[i,j,:])
return im2

In[ ]:
apply_mask(im_2[1:4,1:4])

In[42]:
get_mean_filter(im_2)

In[44]:
s_1=im_2[3:6,10:13]

In[45]:
s_1.sort()
s_1

In[ ]:
s_1=im_2[3:6,10:13].rsahpe(1,9)
s_1
