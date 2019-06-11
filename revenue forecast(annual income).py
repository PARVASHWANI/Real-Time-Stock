#!/usr/bin/env python
# coding: utf-8

# In[30]:


#https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL


# In[31]:


import json,requests


# In[32]:


base_url="https://financialmodelingprep.com/api/v3/financials/income-statement/"
sy = input("Enter NASDAQ Symbol:-")
complete_url = base_url + sy


# In[33]:


respond = requests.get(complete_url)


# In[34]:


x = respond.json()


# In[35]:


x


# In[36]:


float(x["financials"][0]["Revenue"])/100000


# In[37]:


revenues = list()
for i in range(0,10):
    revenues.append(float(x["financials"][i]["Revenue"])/100000)


# In[38]:


revenues.reverse()


# In[39]:


dates =list()
for j in range(0,10):
    dates.append(x["financials"][j]["date"])


# In[40]:


dates.reverse()


# In[41]:


from matplotlib import pyplot as plt


# In[42]:


plt.plot(dates,revenues)
plt.bar(dates,revenues)


# In[ ]:
