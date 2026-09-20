#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd


# In[35]:


df =pd.read_csv("../../datasets/employees.csv")
df.head()


# ## Encoding
# 

# In[36]:


from sklearn.preprocessing import OneHotEncoder
encoder=OneHotEncoder(sparse_output=False,handle_unknown='ignore',drop='first').set_output(transform='pandas')


# In[37]:


ohetransform=encoder.fit_transform(df[["Department",'Education','City']])


# In[38]:


ohetransform


# ## Combine the encoded cartegories with the numeric features

# In[39]:


from sklearn.compose import ColumnTransformer


# In[43]:


preprocessor=ColumnTransformer(
    transformers=[
        ('cat',OneHotEncoder(sparse_output=False),['Department','Education','City'])
    ],
    remainder='passthrough'
).set_output(transform='pandas')


# In[44]:


df=preprocessor.fit_transform(df)
df

