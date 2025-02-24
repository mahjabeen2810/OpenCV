#!/usr/bin/env python
# coding: utf-8

# In[24]:


import cv2


# In[35]:


image=cv2.imread('C:\\Users\\91944\\Desktop\\cv2\\a1.jpg')
B, G, R= cv2.split(image)


# In[41]:


#correlation channels are separated
cv2.imshow('original', image)
cv2.waitKey(0)

cv2.imshow('blue', B)
cv2.waitKey(0)

cv2.imshow('Green', G)
cv2.waitKey(0)

cv2.imshow('red', R)
cv2.waitKey(0)

cv2.destroyAllWindows()


# In[ ]:




