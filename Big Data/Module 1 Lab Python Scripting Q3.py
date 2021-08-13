#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#create a file handle
Names= open('names.txt', "r")


# In[3]:


# set total and count
total = 0
count = 0


# In[4]:


#iterate over, strip spaces, split string, define age, compute total, and iterate count
for line in Names:
    line =  line.strip()
    FName = line.split()
    age = int(FName[-1])
    total = total + age
    count = count + 1


# In[5]:


# compute avg and print
avg = total/count
print(avg)


# In[6]:


Names.close()


# In[ ]:




