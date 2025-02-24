#!/usr/bin/env python
# coding: utf-8

# # Edge Detection
# 
# The process of image detection involved detecting sharp edge in the image.

#  ## Canny edge detector
# The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a  wide range of edges in images. it was developed by john F. Canny in 1986

# The canny edge detection algorithm is composed of 5 steps:
#   1. Noise reduction-Gaussian,median..etc
#   2. Gradient calculation -
#   3. Non-maximum suppression
#   4. Double threshold
#   5. Edge Tracking by Hysteresis.

# In[3]:


import cv2
import numpy as np

FILE_NAME='C:\\Users\\EIT\\Desktop\\opencv2\\flo1.jpg'

img=cv2.imread(FILE_NAME)


# In[4]:


#Canny edge detection.
edges=cv2.Canny(img,100,200)

#save
cv2.imwrite('flower 1 edge detection canny.jpg',edges)


# In[ ]:




