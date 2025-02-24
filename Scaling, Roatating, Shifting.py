#!/usr/bin/env python
# coding: utf-8

# # Application of Filtering in Real-life
# 
# * Image Prcessing
# * Tele-communication
# * Audio recording
# * Computer graphics
# * Television
# * Control system,etc.

# ## Scaling, Rotating, Shifting, and Edge detection
# 
# Scaling am Image: Scaling opration incrases/reduces size of an image.
# interpolation: Interpolation is a method of estimating values between knowns data points

# In[1]:


import cv2
import matplotlib.pyplot as plt
FILE_NAME='C:\\Users\\EIT\\Desktop\\opencv2\\monalisa.jpg'
img=cv2.imread(FILE_NAME)


# In[7]:


#Get number of pixel horizontally and vertically
(hieght, width)=img.shape[:2]


# In[8]:


#Specify the size of the image along with interploation methods.
#cv2.INTER_AREA is used for shirking,whereas cv2.INTER_CUBIC
#is used for zooming.
res=cv2.resize(img,(int(width/3),int(hieght/3)),interpolation=cv2.INTER_CUBIC)


# In[10]:


#Write image back to folder
cv2.imwrite('monolisaresult.jpg',res)


# ## Try-except
# 
# * try: the code with the exception to catch. if an exception is raised, it jumps stright into the except block
# * except: this code is only executed if an exception occured in the try block. The except block is required with a try block, even if it contains only the pass statement. it may be combined with the else.

# # IMAGE ROTATION
# 
# Images can be rotated to any degree clockwise or otherwise. We just need to define rotation matrix listing rotation point, degree of rotation and the scaling factor.

# In[11]:


import cv2
import numpy as np

FILE_NAME='C:\\Users\\EIT\\Desktop\\opencv2\\monalisa.jpg'

img=cv2.imread(FILE_NAME)


# In[12]:


#shape of image in terms of pixels.
(rows, cols)=img.shape[:2]


# In[13]:


# getRotationMatrix2D creates a matrix needed for tranformation.
# We want matrix for rotation w.r.t center to 45 degree without scaling.


# In[14]:


M= cv2.getRotationMatrix2D((cols/2,rows/2),-50,1)#POSITIVE VALUE,NEGATIVE VALUE(50,-50)
res=cv2.warpAffine(img,M,(cols,rows))#warpAffine to implement simple remapping routines.


# In[15]:


#Write image back to Folder
cv2.imwrite('MONOLISA_ROTATE.jpg',res)


# # Translating an Image
# 
# Transalating an image means shifting it within a given frame of reference.

# In[16]:


import cv2
import numpy as np

FILE_NAME='C:\\Users\\EIT\\Desktop\\opencv2\\monalisa.jpg'


# In[19]:


M=np.float32([[1,0,200],[0,1,150]])

img=cv2.imread(FILE_NAME)

(rows, cols)=img.shape[:2]

#apply shifting
res=cv2.warpAffine(img,M,(cols,rows))

#save
cv2.imwrite('translate_mono2.jpg',res)


# In[ ]:




