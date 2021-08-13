#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#create a file handle
Log = open('user_access.log', "r")


# In[3]:


#create dictionary
user_access = {}


# In[4]:


#iterate over, split string on semicolon, strip, and store user ID and access time
for line in Log:
    user_id, time = line.split(';')
    user_access[user_id.strip()] = time.strip()


# In[5]:


Log.close()


# In[6]:


print('Last access time for user ID 000397:', user_access['000397'])
print('Last access time for user ID 126052:', user_access['126052'])


# In[ ]:




