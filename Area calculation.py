#!/usr/bin/env python
# coding: utf-8

# # Calculate the area of an image

# ## Algorithm:
# 1. Import the matplotlib.pyplot module
# 2. Import an image using the imread() method.
# 3. Use the shape attribute of the image to get the height and width of the image. it fetches the number of channels in the image.
# 4. Calcualte the area as, area = height * width.
# 5. disply the area.

# In[4]:


import matplotlib.pyplot as plt
img=plt.imread('C:\\Users\\EIT\\Desktop\\opencv2\\flo1.jpg')


# In[5]:


#fetch the height and width
height,width,_=img.shape

#area is calculated as 'heigth x width'
area=height*width
print('Area of the image is:',area)

