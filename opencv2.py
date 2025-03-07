#!/usr/bin/env python
# coding: utf-8

# # Reading methods:

# ### 1:PIL

# In[27]:


#1:PIL
from PIL import Image

img=Image.open('C:\\Users\\EIT\\Desktop\\opencv2\\bfruit.png')
img.show()


# ### 2:Usinng matplotlib module

# In[28]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=Image.open('C:\\Users\\EIT\\Desktop\\opencv2\\bfruit.png')
img.show(img)


# ### 3:Using imageio with matplotlib

# In[34]:


import imageio
import matplotlib.pyplot as plt

img=Image.open('C:\\Users\\EIT\\Desktop\\opencv2\\bfruit.png')
plt.imshow(img)


# ### 4:Using opencv()

# In[40]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('bfruit.png')
img.shape


# ### 5:Opencv with matplotlib module

# In[41]:


import cv2 as cv
import matplotlib.pyplot as plt

#Read the image in grayscale mode
img=cv2.imread('C:\\Users\\EIT\\Desktop\\opencv2\\bfruit.png')
plt.imshow(img)


# ### convert BGR to RGB

# In[43]:


RGBimg=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(RGBimg)


# ## SAVING IMAGE

# In[49]:


imgpht=cv2.imwrite('C:\\Users\\EIT\\Desktop\\opencv2\\img.png',img)


# ## Opencv add text 

# In[5]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt')


# In[6]:


img=cv2.imread('C:\\Users\\EIT\\Desktop\\opencv2\\fff.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)


# In[7]:


img_2=np.copy(img)
text='Flower_Name'
orgin=(1000,500)
font=cv2.FONT_HERSHEY_COMPLEX
font_scale=10
color=(000,139,171)
thickness=60


# In[8]:


img_2=cv2.putText(img_2,text,orgin,font,font_scale,color,thickness)
plt.imshow(img_2)


# ### create a frame and add text

# In[83]:


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# In[94]:


image=np.zeros((400,400,3),dtype='uint8')
image[:]=0,0,255


# In[95]:


cv.putText(image,'opencv',(50,200),cv.FONT_ITALIC,3,(246,246,247),4)
plt.imshow(image)
#cv.waitKey(0)


# In[ ]:




