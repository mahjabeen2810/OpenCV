#!/usr/bin/env python
# coding: utf-8

# # Draw rectangle on an image
# 
# syntax: Rectangle(x,y,width,height,angle=0.0,**kwargs)
# parameteres:
# * xy:     Lower left point to start the rectangle plotting
# * width:  width of the rectagle
# * hieght: Height of the rectangle
# * angle:  Angle of the rectangle.

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np


# In[33]:


x=np.array(Image.open('C:\\Users\\EIT\\Desktop\\opencv2\\flo2.jpg'))
plt.imshow(x)


# In[50]:


#create figure and axis
fig, ax = plt.subplots(1)


#display the image
ax.imshow(x)

#create rectangle patch
rect=patches.Rectangle((450,500),700,700,linewidth=2,edgecolor='white',facecolor='none')

#Add to patch to the Axes
ax.add_patch(rect)
plt.show()


# # DRAW FILL COLOR

# In[51]:


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np


# In[66]:


x=np.array(Image.open('C:\\Users\\EIT\\Desktop\\opencv2\\leaf1.jpg'))
plt.imshow(x)


# In[68]:


#create figure and axis
fig, ax = plt.subplots(1)


#display the image
ax.imshow(x)

#create rectangle patch
rect=patches.Rectangle((500,700),400,500,linewidth=3,edgecolor='white',facecolor='r')

#Add to patch to the Axes
ax.add_patch(rect)
plt.show()


# In[ ]:




