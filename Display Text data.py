#!/usr/bin/env python
# coding: utf-8

# Sytax:
# 
# cv2.putText(src,text,org,font,scale,color,thickness,lineType,bottomLeftOrgin)

# Img: Source image or image over which we have to draw the line
# pt1: Starting coordinates of the line segment.
# pt2: Ending coordinates of the line segment
# color: The color of the line
# Thickness: Thickness of the line
# LineType: Type of the line offered by OpenCV
# Shift: Fractional bits in the point coordinates

# In[1]:


#bottomLeftOrgin: it specifies the org to be bottom-left corner if true,otherwise, top-left corner.


# In[10]:


#Create a blank image
import cv2
import matplotlib.pyplot as plt
import numpy as np
blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(blank_img)


# In[22]:


#Text
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,text='DILSHAD',org=(125,275),fontFace=font,fontScale=2,color=(125,125,240),thickness=5,lineType=cv2.LINE_AA)
plt.imshow(blank_img)


# In[ ]:




