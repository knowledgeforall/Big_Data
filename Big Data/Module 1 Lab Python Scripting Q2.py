#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#create a file handle
Names= open('names.txt', "r")


# In[3]:


#iterate over, strip spaces, split string, and print
for line in Names:
    line = line.strip()
    FName = line.split()
    print(FName[0])


# In[4]:


Names.close()


# In[ ]:




