#!/usr/bin/env python
# coding: utf-8

# # PLOT A POINT OR LINE IN A IMAGE

# dway a small marker "v" point in a image

# In[1]:


from matplotlib import image
import matplotlib.pyplot as plt


# In[9]:


#to read the image stored in the working directory
data=image.imread('C:\\Users\\EIT\\Desktop\\opencv2\\ker1.jpg')


# In[10]:


#to draw a line from (200,300) to (500,100)
x=[1200,1500]
y=[1300,1500]
plt.plot(x,y,color='white',linewidth=5)
plt.imshow(data)
plt.show()


# # Draw two interescting line crossing each other to make X

# In[11]:


from matplotlib import image
import matplotlib.pyplot as plt


# In[60]:


#to read the image stored in the working directory
data=image.imread('C:\\Users\\EIT\\Desktop\\opencv2\\flo1.jpg')


# In[61]:


#to draw first line from (1500,2400) to (2500,3100)
#to draw second line from (2150,2100) to (2150,3400)
x1=[1500,2500]
y1=[2400,3100]
x2=[2150,2150]
y2=[2100,3400]
plt.plot(x1,y1,x2,y2,color='white',linewidth=3)
plt.axis('off')
plt.imshow(data)
plt.show()


# In[ ]:




