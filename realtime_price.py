#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL
import json,requests


# In[2]:


base_url = "https://financialmodelingprep.com/api/v3/stock/real-time-price/"
symbol = input("Enter NASDQE Symbol:-")
complete_url = base_url + symbol


# In[3]:


complete_url


# In[4]:


response = requests.get(complete_url)


# In[5]:


data = response.json()
x = data["symbol"]


# In[11]:


z = data['price']


# In[14]:


print("Symbol Entered:-",x)
print("Price(RealTime):-",z)
