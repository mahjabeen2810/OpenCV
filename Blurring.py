#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


image=cv2.imread('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\hum3.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


# In[6]:


#Gaussian blur
import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\hum3.jpg')

blurimg=cv2.blur(image,(7,7),0)
plt.imshow(cv2.cvtColor(blurimg, cv2.COLOR_BGR2RGB))


# In[7]:


# Median blur
import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\hum3.jpg')

meadian=cv2.medianBlur(image,5)
plt.imshow(cv2.cvtColor(meadian, cv2.COLOR_BGR2RGB))


# In[8]:


# Bilateral blur
import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('C:\\Users\\OAP6\\Desktop\\Nayan-opencv\\hum3.jpg')

bilateral=cv2.bilateralFilter(image,9,75,75)
plt.imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB))


# In[ ]:




