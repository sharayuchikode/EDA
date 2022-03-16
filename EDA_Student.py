#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from plotly.offline import iplot
import plotly as py
import plotly.tools as tls
import cufflinks as cf
py.offline.init_notebook_mode(connected=True) #Turning on notebook mode 
cf.go_offline()


# In[3]:


data=pd.read_csv(r"C:\Users\Sharayu\Downloads\StudentsPerformance.csv")
data


# In[5]:


data.shape


# In[6]:


data.info()


# In[7]:


data.dtypes


# In[8]:


data.describe()


# In[15]:


data.columns


# ### Missing Values

# In[16]:


data.isnull().sum()


# In[18]:


data.duplicated().sum()


# ### Visulization

# In[19]:


data.boxplot()

The circles represent outliers in the dataset. However,  it is possible for a student to score extremely low marks in a test. 
# In[23]:


sns.distplot(data['math score'])


# In[ ]:


This graph shows the bell curved. And mean of the maths score students i about 65.


# In[24]:


sns.distplot(data['reading score'])


# In[ ]:


This graph shows the bell curved. And mean of the maths score students i about 70.


# In[25]:


sns.distplot(data['writing score'])

This graph shows the bell curved. And mean of the maths score students i about 70.
# In[31]:


c=data.corr()
sns.heatmap(c,annot=True,square=True)
plt.yticks(rotation=0)
plt.show()

Reading score has a correlation coefficient of 0.95 with the writing score. Math score has a correlation coefficient of 0.82 with the reading score, and 0.80 with the writing score.
# In[34]:


sns.relplot(x='math score',y='writing score',hue='gender',data=data)

It shows the difference between male and female.Female have more writing score than male.
# In[43]:


data.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean().plot(figsize=(12,8))

It is very clear from this graph that students whose parents are more educated than others (master’s degree, bachelor’s degree, and associate’s degree) are performing better on average than students whose parents are less educated (high school).
# In[45]:


data.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean().plot(kind='barh', figsize=(10,10))

it is very clear that students who have completed the test preparation course have performed better, on average, as compared to students who have not opted for the course.
# In[ ]:




