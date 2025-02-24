#!/usr/bin/env python
# coding: utf-8

# # Interpolation Schemes:

# Interpolation calculates what the color or value of a pixel "should" be and this needed when we resize the image but want the same information.

# In[2]:


from PIL import Image
import matplotlib.pyplot as plt

#Reading image file
img=Image.open('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\for1.jpg')

#resizing the image
img.thumbnail((50,50),Image.ANTIALIAS)
imgplot=plt.imshow(img)


# # BICUBIC VALUE USED FOR INTERPOLATION

# In[9]:


from PIL import Image
import matplotlib.pyplot as plt

#Reading image file
img=Image.open('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\monolisa.jfif')

#resizing the image
img.thumbnail((30,30),Image.ANTIALIAS)

#bicubic used for interpolation
imgplot=plt.imshow(img,interpolation='bicubic')


# # SINC VALUE USED FOR INTERPOLATION

# In[10]:


from PIL import Image
import matplotlib.pyplot as plt

#Reading image file
img=Image.open('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\monolisa.jfif')

#resizing the image
img.thumbnail((30,30),Image.ANTIALIAS)

#sinc used for interpolation
imgplot=plt.imshow(img,interpolation='sinc')


# In[ ]:




