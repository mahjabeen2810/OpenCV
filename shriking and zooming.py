#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = 'C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\nat2.jpg'
img=cv2.imread(FILE_NAME)

# Get number of pixel horizontally and vertically.
hieght, width, channels = img.shape


# In[3]:


# specify the size of image along with interpolation
# cv2.INTER_AREA is used for shirking, whereas cv2.INTER_CUBIC
# is used for zooming.
res=cv2.resize(img,(int(width/2),int(hieght/2)),interpolation=cv2.INTER_AREA)


# In[6]:


# Write image back to disk
cv2.imwrite('nat2_half.jpg',img_half)
print('Error while reading files')


# In[55]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\nat2.jpg", 1)
orginal=image
plt.title('original')
plt.imshow(cv2.cvtColor(orginal, cv2.COLOR_BGR2RGB))

# Write image back to disk
cv2.imwrite('nat2_og.jpg',orginal)


# In[56]:


#Interpolation Nearest
image = cv2.imread("C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\nat2.jpg", 1)
# Loading the image

stretch_near = cv2.resize(image, (780, 540),interpolation = cv2.INTER_NEAREST)

plt.title('Interpolation Nearest')
plt.imshow(cv2.cvtColor(stretch_near, cv2.COLOR_BGR2RGB))

# Write image back to disk
cv2.imwrite('nat2_stretch_near.jpg',stretch_near)


# In[57]:


image = cv2.imread("C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\nat2.jpg", 1)
# Loading the image

#bigger
bigger = cv2.resize(image, (1050, 1610))

plt.title('bigger')
plt.imshow(cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB))

# Write image back to disk
cv2.imwrite('nat2_bigger.jpg',bigger)


# In[58]:


image = cv2.imread("C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\nat2.jpg", 1)
# Loading the image

#half
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)

plt.title('half')
plt.imshow(cv2.cvtColor(half, cv2.COLOR_BGR2RGB))

# Write image back to disk
cv2.imwrite('nat2_half.jpg',half)


# In[ ]:




