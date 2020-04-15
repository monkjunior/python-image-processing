#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 
import numpy as np 
import matplotlib.pyplot as plt


# In[2]:


bean = cv2.imread("bean.jpg")
print(bean.shape)
bean = cv2.imread("bean.jpg", cv2.IMREAD_GRAYSCALE)
print(bean.shape)


# In[3]:


def linearTransform(pix, r1, s1, r2, s2): 
    if (0 <= pix and pix <= r1): 
        return (s1 / r1)*pix 
    elif (r1 < pix and pix <= r2): 
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1 
    else: 
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2 


# In[4]:


# Define parameters. 
r1 = 60
s1 = 30
r2 = 130
s2 = 200


# In[8]:


# Vectorize the function to apply it to each value in the Numpy array. 
linearTrans_vec = np.vectorize(linearTransform) 
  
# Apply contrast stretching. 
contrast_stretched = linearTrans_vec(bean, r1, s1, r2, s2)

#plt.imshow(bean, cmap='gray', interpolation='bicubic')
#plt.show()
cv2.imwrite("bean_contrast.png", contrast_stretched)





