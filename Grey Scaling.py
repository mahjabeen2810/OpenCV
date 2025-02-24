#!/usr/bin/env python
# coding: utf-8

# # GREY SCALLING

# In[1]:


#GRAY SCALING IMAGE using cv
import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\hum3.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))


# In[2]:


# Grey scaling using matplotlib
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#open image
image=Image.open('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\hum3.jpg')

#convert image to black and white pixels
gray_image=image.convert('L')

#convert image to Numpy array
gray_image_array=np.asarray(gray_image)

#disply image on grayscale
plt.imshow(gray_image_array,cmap='gray')
plt.show()


# In[ ]:




