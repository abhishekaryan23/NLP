#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tweepy import API 
from tweepy import Cursor
from tweepy import OAuthHandler
from textblob import TextBlob


# In[ ]:


#function to calculate percentage
def percentage(part, whole):
    return 100 *float(part)/float(whole)


# In[ ]:


# User credential for acessing the Twitter APIs
consumer_key="consumer key"
consumer_secret="consumer key secret"
access_token="access token"
access_secret="access token secret"


# In[ ]:


#authenticating twitter API using your keys
auth = OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_token, access_secret)
api =API(auth)


# In[ ]:


#taking input from user about keyword/hashtags & No. of tweets to analyze
search_term= input("Enter keyword/hashtag to search about:")
no_of_searchterm=int(input("No. of tweets to analyze:"))


# In[ ]:


tweets= Cursor(api.search, q=search_term).items(no_of_searchterm)


# In[ ]:


#initializing the variable to check polarity
positive=0
negative= 0
neutral= 0
polarity=0


# In[ ]:


for tweet in tweets:
    analysis= TextBlob(tweet.text)
    polarity+= analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity==0):
        neutral+= 1
    elif(analysis.sentiment.polarity<0.00):
        negative+= 1
    elif(analysis.sentiment.polarity>0.00):
        positive+= 1
polarity


# In[ ]:


positive= percentage(positive,no_of_searchterm)
negative= percentage(negative,no_of_searchterm)
neutral= percentage(neutral,no_of_searchterm)
#fromating the variables
positive= format(positive,'.2f')
negative= format(negative,'.2f')
neutral= format(neutral,'.2f')


# In[ ]:


print('By analyzing '+str(no_of_searchterm)+' of tweets, sentiments about '+str(search_term)+' is:')
if (polarity == 0):
    print("Neutral")
elif(polarity < 0):
    print("Negative")
elif(polarity > 0):
    print("Positive")


# In[ ]:


# creating a pie plot of the result obtained
labels=['Neutral['+str(neutral)+'%]','Negative['+str(negative)+'%]','Positive['+str(positive)+'%]']
sizes=[neutral,negative,positive,]
colors=['yellow','red','green']
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc='best')
plt.title('Sentiments relating to '+str(search_term))
plt.axis('equal')
plt.tight_layout()
plt.show()

