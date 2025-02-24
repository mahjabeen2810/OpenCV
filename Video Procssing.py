#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2


# In[10]:


vid_capture=cv2.VideoCapture('C:\\Users\\EIT\\Desktop\\opencv2\\uni.mp4')

if (vid_capture.isOpened()==False):
    print('Error opening the video file')
    
else:
    frame_count=vid_capture.get(7)
    print('Frame count :',frame_count)
    
while(vid_capture.isOpened()):
    ret,frame=vid_capture.read()
    
    if ret==True:
        cv2.imshow('Frame',frame)
        key=cv2.waitKey(2)
        if key==ord('q'):
            break
        
        
    else:
        break


# In[11]:


#Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()


# In[ ]:




