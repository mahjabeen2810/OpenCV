#!/usr/bin/env python
# coding: utf-8

# This function is used to draw a line segment that connect any two points. it draws a line between points p1 and point p2. The line gets clipped by the boundaries of the image.

# Img: Source image or image over which we have to draw the line
# pt1: Starting coordinates of the line segment.
# pt2: Ending coordinates of the line segment
# color: The color of the line
# Thickness: Thickness of the line
# LineType: Type of the line offered by OpenCV
# Shift: Fractional bits in the point coordinates

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Creating a blank image
blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
#displying blank image
plt.imshow(blank_img)


# In[23]:


# Creating line
# Creating line using the cv2.line function
#cv2.line(image,start_point,end_point,color,thickness)
cv2.line(blank_img,pt1=(50,50),pt2=(50,450),color=(0,255,0),thickness=5)
# Displying the image with the line created on it
plt.imshow(blank_img)


# In[ ]:




