#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_excel('C:/Users/96132/Desktop/ecousdata.xlsx', sheet_name='GDP')
data.head()


# In[4]:


## getting the correlation between GDP and consumption


# In[7]:


data1 = data[['gross domestic product', 'personal consumption expenditures']]
correl = data1.corr(method='pearson')


# In[8]:


correl


# In[9]:


## mean of investment over the years


# In[10]:


inv = data['fixed investment'].mean()


# In[11]:


inv


# In[12]:


## a rolling time serie mean over gdp


# In[13]:


gdp = data['gross domestic product, current dollars'].rolling(10).mean()
gdp


# In[14]:


gdp.plot


# In[15]:


## a plot of imports


# In[16]:


imp = data['imports'].plot


# In[17]:


imp


# In[18]:


gdp.plot()


# In[ ]:





# In[ ]:




