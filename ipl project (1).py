#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Loading the required Libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[3]:


#Loading the ipl matches dataset 
ipl=pd.read_csv('E:/New folder/matches.csv')


# In[4]:


#having a glance at the first five records of the dataset
ipl.head()


# In[5]:


#Lookin the number of rows and columns in the dataset
ipl.shape


# In[12]:


#getting the frequency of most man of the match awards
ipl['player_of_match'].value_counts()[0:10]


# In[19]:


list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[22]:


#making a bar plot for the top 5 players with most man of the match awards
plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="g")
plt.show()


# In[23]:


#getting the frequency of result column
ipl['result'].value_counts()


# In[29]:


#Finding out the number of toss wins w.r.t each team
ipl['toss_winner'].value_counts()[0:5]


# In[30]:


list(ipl['toss_winner'].value_counts()[0:5].keys())


# In[35]:


#Extracting the records where a team won batting first
batting_first=ipl[ipl['win_by_runs']!=0] 


# In[36]:


#looking at the heaad
batting_first.head()


# In[37]:


#making a histogram
plt.figure(figsize=(5,7))
plt.hist(batting_first['win_by_runs'])
plt.title("Distribution of runs")
plt.xlabel("Runs")
plt.show()


# In[38]:


#Finding out the number of wins w.r.t each team after batting first
batting_first['winner'].value_counts()


# In[39]:


#making a bar-plot for top 3 teams with most wins after batting first
plt.figure(figsize=(6,6))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","green"])


# In[44]:


#making a pie chart
plt.figure(figsize=(6,6))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[48]:


#extracting those records where a team wons after batting second
batting_second=ipl[ipl['win_by_wickets']!=0]


# In[50]:


batting_second.head()


# In[59]:


#making a histogram for frequency of wins w.r.t number of wickets
plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[60]:


#Finding out the frequency of number of wins w.r.t each time after batting second
batting_second['winner'].value_counts()


# In[67]:


#Making a bar-plot for top 3 teams with most wins after batting second
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=["purple","red","blue"])
plt.show()


# In[71]:


#Making a pie chart for distribution of most wins after second batting
plt.figure(figsize=(5,5))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[74]:


#looking at the number of matches played each season
ipl['Season'].value_counts()


# In[76]:


#Looking at the number of matches in each city
ipl['city'].value_counts()


# In[77]:


#Finding out how many times a team has won the match after winning the toss
import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])


# In[ ]:




