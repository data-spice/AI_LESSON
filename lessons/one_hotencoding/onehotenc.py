#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[8]:


data='../../datasets/employees.csv'
df=pd.read_csv(data)
df.head()


# In[9]:


from sklearn.preprocessing import OneHotEncoder
encoder=OneHotEncoder(
    sparse_output=False,
    handle_unknown='ignore',
    drop='first'
).set_output(transform='pandas')


# In[14]:


ohetransform=encoder.fit_transform(df[['City']])
ohetransform.head()


# In[19]:


df=pd.concat([df,ohetransform],axis=1).drop(columns=['City'])
df

