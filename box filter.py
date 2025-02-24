#!/usr/bin/env python
# coding: utf-8

# # Box Filter
# 
# We can perform this filter using the boxfilter() function. It is similar to the averaging blur operation. The syntax of the function is given below: cv2. boxfilter(src, dst, ddepth, ksize, anchor, normalize, bordertype)
# 
# ## Parameters:
# 
# * src- It denotes the source of the image. It can be an 8-bit or floating-point, 1- channel image.
# * dst- it denotes the destination image of the same size. Its type will be the same the src image.
# * ddepth- It denotes the output image depth. 
# * ksize- It blurs the kernel size.
# * anchor- It denotes the anchor points. By default, its value Point to coordinates (1,1), which means that the anchor is at kernel center. 
# * normalize - It is the flag, specifying whether the kernel should be normalized or not.
# * borderType - An integer object represents the type of the border used.

# In[12]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

#using imread('path') and 0 denotes read as grayscale image
img = cv2.imread("C:\\Users\\EIT\\Desktop\\opencv2\\flo2.jpg") 


# In[15]:


cv2.imshow(img)


# In[ ]:


#This is necessary to be required so that the image doesn't close immediately. #It will run continuously until the key press.
img_1 = cv2.boxFilter(img, 0, (7,7), img, (-1,-1), False, cv2.BORDER_DEFAULT) #cv2.imshow("Image',img_1) cv2.waitKey(0)
cv2.imshow('Image',img_1)
cv2.waitKey(0)

#cv2.destroyAllWindows()

