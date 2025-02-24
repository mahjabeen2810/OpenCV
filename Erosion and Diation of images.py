#!/usr/bin/env python
# coding: utf-8

# # Erosion and Dilation of images
# 
# Morphological operations are a set of operations that process images based on shapes. They apply a structuring element to an input image and generate an output image.
# 
# The most basic morphological operations are two: Erosion and Dilation 
# Basics of Erosion:
# * Erodes away the boundaries of the foreground object 
# * Used to diminish the features of an image.
# 
# Basics of dilation:
# * Increases the object area
# * Used to accentuate features
# 
# Uses of Erosion and Dilation: 
# 1. Erosion:
# * It is useful for removing small white noises.
# * Used to detach two connected objects etc.
# 
# 2. Dilation:
# * In cases like noise removal, erosion is followed by dilation. Because, erosion removes white         noises, but it also shrinks our object. So we dilateit. Since noise is gone, they won't come back,   but our object area increases.
# * It is also useful in joining broken parts of an object.

# ## program: Erosion, Dilation:

# In[21]:


#program:Erosion,Dilation
import cv2
import numpy as np

img=cv2.imread('C:\\Users\\EIT\\Desktop\\opencv2\\flo2.jpg',0)


# In[22]:


#Taking a matrix of size 5 as the kernel
import numpy as np
kernal=np.ones((5,5),np.uint8)

#kernel is the matrix with which image
img_erosion=cv2.erode(img,kernal,iterations=1)
img_dilation=cv2.dilate(img,kernal,iterations=1)


# In[23]:


cv2.imshow('input',img)
cv2.imshow('Erosion',img_erosion)
cv2.imshow('Dilation',img_dilation)
cv2.waitKey(0)

