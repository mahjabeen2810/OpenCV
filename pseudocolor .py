#!/usr/bin/env python
# coding: utf-8

# # Applying pseudocolor to image

# applying pseudocolor to image pseudocolor is useful for enhancing contrast of image. importing pyplot and image from matplotlib

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as img


# In[3]:


#reading png image
im=img.imread('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\sea1.jpg')


# In[4]:


#applying pseudocolor
#default value of colormap is used.
lum=im[:,:,0]


# In[5]:


#show image
plt.imshow(lum)


# In[ ]:




