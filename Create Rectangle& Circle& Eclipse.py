#!/usr/bin/env python
# coding: utf-8

# # Rectangle
# This Function is used to create a rectangle in OpenCV. A rectangle can be defined as a plane figure with four straight sides and right angles, and unequal adjacent sides. The opposite corners of the rectangle represent the two points pt1 and pt2.

# Syntax:
# cv2.rectangle(img,pt1,pt2,color,thickness,lineType,shift)

# Img: Source image or image over which we have to draw the line
# pt1: Starting coordinates of the line segment.
# pt2: Ending coordinates of the line segment
# color: The color of the line
# Thickness: Thickness of the line
# LineType: Type of the line offered by OpenCV
# Shift: Fractional bits in the point coordinates

# In[11]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[12]:


blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(blank_img)


# In[13]:


#Rectangle
cv2.rectangle(blank_img,pt1=(100,100),pt2=(400,400),color=(0,255,0),thickness=7)
plt.imshow(blank_img)


# # Circle

# syntax:
# cv2.circle(img,centre,radius,color,thikness,lineType,shift)

# In[14]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[15]:


blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(blank_img)


# In[39]:


cv2.circle(blank_img,center=(250,250),radius=150,color=(255,0,0),thickness=3)
plt.imshow(blank_img)


# # Drawing a filled circle

# In[ ]:





# In[40]:


#create a blank image
blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(blank_img)


# In[41]:


#Fill color
cv2.circle(blank_img,center=(250,250),radius=150,color=(255,0,255),thickness=3)
plt.imshow(blank_img)


# # Create eclipse
# syntax: 
# cv2.ellipse(src,center,axes,angle,startAngle,endAngle,color,thickness,lineType,shift)

# In[42]:


#create a blank image
import cv2
import numpy as np
import matplotlib.pyplot as plt
blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(blank_img)


# In[43]:


#Create Eclipes
cv2.ellipse(blank_img,(250,250),(90,50),0,0,360,(0,0,255),10)
plt.imshow(blank_img)


# In[ ]:




