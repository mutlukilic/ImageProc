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
