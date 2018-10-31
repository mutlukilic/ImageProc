#a-) 28x28 boyutlarında içeriği 0 ve 1 olan bir matris üretiniz.
# --- my_create_m(): return result=[]28x28  içeriği 0 1 matris
#b-) A şıkkında üretilen matrisle 1 leri içeren MBR dikdörtgeni üreten fonksiyonu yazınız
# --- def my_MBR (matrix_block) 1 leri içeren en küçük dikdörtgeni değeri elde edicek
#c-) Kendisine aktarılan iki vektörün benzerliğini return eden fonksiyonu yazınız.
# --- def ... (a,b)  skaler çarpımı göndercek geri
#d-) A şıkkında yazdığınız fonksiyonu kullanarak 100 farklı matris elde edip birinci 
#üretilen ile diğerlerini karşılaştırıp(distance) yakınlığını ve benzerliğini listeleyiniz
# --- 100 tane A daki fonk çağır ordaki 100 tanesini 1. ile karşılaştır
# haftaya mnist data

import numpy as np
import matplotlib.pyplot as plt
import random as random

def my_create_m():
    return np.random.randint(0,2,(28,28))
def my_MBR(matrix_block):
    print(my_create_m())
    
 def matrix_create_28_by_28_with_0_1():
    my_matrix=np.zeros((28,28))
    for i in range(28):
        for j in range(28):
            my_matrix[i,j]=random.randint(0,1)
    return my_matrix

def MBR_create_28_by_28_with_0_1(matrix_a):
    m=matrix_a.shape[0]
    n=matrix_a.shape[1]
    x_min=m
    x_max=0
    y_min=n
    y_max=0
    for i in range(m):
        for j in range(n):
            if((matrix_a[i,j]==0) and x_min>i):
                x_min = i
            if((matrix_a[i,j]==0) and x_min<i):
                x_min = i
            if((matrix_a[i,j]==0) and y_min>j):
                x_min = i
            if((matrix_a[i,j]==0) and y_max<j):
                x_min = i
    return(x_min,x_max,y_min,y_max)

def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    for i in range(m):
        for j in range(n):
            my_similarity = my_similarity+character_a[i,j]*character_b[i,j]
    return my_similarity
    
c_1=matrix_create_28_by_28_with_0_1()
c_2=matrix_create_28_by_28_with_0_1()
get_similarity(c_1,c_2)

def get_similarity_for_100_characters(kac_karakter=100):
    characters=[]
    for i in range(100):
        new_char = matrix_create_28_by_28_with_0_1()
        characters.append(new_char)
    for i in range(100):
        benzerlik=get_similarity(characters[0],characters[i])
        print("0---"+str(i)+" ",benzerlik)

c_1=matrix_create_28_by_28_with_0_1()
c_2=matrix_create_28_by_28_with_0_1()
get_similarity(c_1,c_2)
get_similarity_for_100_characters(10)
