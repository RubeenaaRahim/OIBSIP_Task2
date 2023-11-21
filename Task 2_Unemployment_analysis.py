#!/usr/bin/env python
# coding: utf-8

# # Unempolyment Analysis with python
# 
# Importing libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')
import calendar


# In[2]:


import datetime as dt

import plotly.io as pio 
pio.templates


# In[3]:


df = pd.read_csv("Unemployment in India.csv")


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.shape


# In[8]:


#checking for null values
df.isna().values.any()


# In[9]:


df.isna().sum()


# In[11]:


df = df.dropna()


# In[12]:


df.isna().sum()


# In[13]:


df.shape


# In[14]:


df.duplicated().sum()


# In[15]:


df.describe()


# In[16]:


df.columns


# In[17]:


df.columns=['State','Date','Frequency','Estimated Unemployment Rate','Estimated Employed','Estimated Labour Participation','Area']


# In[18]:


# to print the state with highest unemployment
print("State with highest Unemployment:-",df['State'].value_counts().idxmax())


# In[19]:


# to print the state with lowest unemployment
print("State with Lowest Unemployment:-",df['State'].value_counts().idxmin())


# In[20]:


#to print the month of unemployment

import datetime as dt
import calendar

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)


# In[21]:


df["Date"]


# In[22]:


df['month_int'] =  df['Date'].dt.month
df['month'] =  df['month_int'].apply(lambda x: calendar.month_abbr[x])


# In[23]:


df["month_int"]


# In[24]:


df["month"]


# In[25]:


#to print the month with highest unemployment

print("Month with highest Unemployment:-",df['month'].value_counts().idxmax())


# In[26]:


#to print the month with lowest unemployment

print("Month with lowest Unemployment:-",df['month'].value_counts().idxmin())


# In[27]:


df.head()


# In[28]:


#drop the unwanted columns

df.drop(columns=['Frequency','month_int'])


# In[30]:


#top 10 states with highest unemployment

df1=df[['State','Estimated Unemployment Rate']].groupby('State').sum().sort_values(by='Estimated Unemployment Rate',ascending=False)


# In[31]:


df1.head(10)


# In[ ]:





# In[ ]:





# # visualisation

# In[32]:


fig=plt.figure()
plot =fig.add_subplot(1,2,1) 
df1[:10].plot(kind="bar",color="green",figsize=(20,10),ax=plot)
plot.set_title("Top 10 States with Highest Unemployment")
plot.set_xlabel("State")
plot.set_ylabel("Number of people unemployed in %")


# In[33]:


# months with highest unemployment

df2 = df[["month","Estimated Unemployment Rate"]].groupby("month").sum().sort_values(by="Estimated Unemployment Rate", ascending  =False)
df2.head(10)


# In[34]:


fig=plt.figure()
plot2=fig.add_subplot(1,2,1)
df2[:12].plot(kind="bar",color="blue",figsize=(20,10),ax=plot2)
plot2.set_title("Months with highest unemployment")
plot2.set_xlabel("Region")
plot2.set_ylabel("Number of People Unemployed (in %)")


# In[ ]:


# To visulize labour participation rate & unemployment rate in each month


IND =  df.groupby(["month"])[['Estimated Unemployment Rate', "Estimated Employed", "Estimated Labour Participation Rate"]].mean()
IND = pd.DataFrame(IND).reset_index()
month = IND.month
unemployment_rate = IND["Estimated Unemployment Rate"]
labour_participation_rate = IND["Estimated Labour Participation Rate"]

fig = go.Figure()

fig.add_trace(go.Bar(x = month, y = unemployment_rate, name= "Unemployment Rate"))
fig.add_trace(go.Bar(x = month, y = labour_participation_rate, name= "Labour Participation Rate"))

fig.update_layout(title="Uneployment Rate and Labour Participation Rate",
                  xaxis={"categoryorder":"array", "categoryarray":["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]})

fig.show()


# In[36]:


# State wise rate of unemplyement

df1 = df[["State","Estimated Employed"]].groupby("State").sum().sort_values(by="Estimated Employed", ascending =False)
df1.head(10)
fig=plt.figure()
ax0=fig.add_subplot(1,2,1)
ax1=fig.add_subplot(1,2,2)

#Unemployed
df1[:10].plot(kind="bar",color="red",figsize=(15,6),ax=ax0)
ax0.set_title("People Unemployed in each State")
ax0.set_xlabel("State")
ax0.set_ylabel("Number of People Unemployed (in %)")

#Employed
df1[:10].plot(kind="bar",color="green",figsize=(15,6),ax=ax1)
ax1.set_title("People Employed in each State")
ax1.set_xlabel("State")
ax1.set_ylabel("Number of People Employed (in %)")


# In[38]:


# bar plot unemployment rate (monthly)

fig = px.bar(df, x='State',y='Estimated Unemployment Rate', animation_frame = 'month', color='State',
            title='Unemployment rate (State)')

fig.update_layout(xaxis={'categoryorder':'total descending'})

fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"]=2000

fig.show()


# # Inferences:
# 1. State with highest Unemployment:- Andhra Pradesh
# 2. State with Lowest Unemployment:- Chandigarh
# 3. Month with highest Unemployment:- May
# 4. Month with lowest Unemployment:- April
# 5. Graph Progress: Higher The labour participation Lower the unemployment rate

# In[ ]:




