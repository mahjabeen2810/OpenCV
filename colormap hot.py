#!/usr/bin/env python
# coding: utf-8

# # COLOR MAP-HOT

# In[5]:


#import pyplot and Image from matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img

#reading png image
im=img.imread('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\p3.png')
lum=im[:,:,0]

#setting colormap as hot
plt.imshow(lum,cmap='hot')
plt.colorbar()


# In[ ]:




