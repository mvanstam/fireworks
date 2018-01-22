
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re



# In[8]:


def cleanText(text):
    text = text.split()
    text = " ".join(text)
    text = text.lower()
    return text

string = 'westerdokseiland  '

print(cleanText(string))


# In[9]:


tweet_df = pd.read_csv('large_file_sentiment.csv')

loc_df = pd.read_csv('Buurten.csv', encoding = "ISO-8859-1")
loc_df

loc_df['clean_loc'] = loc_df['buurten'].apply(lambda x: cleanText(x))


loc_list = np.array(loc_df.clean_loc)
loc_list


# In[11]:


# set counter
x = 0 

def matchTweet(text, loc_list):
    global x 
    
#     print(text)
    
    locations = []
    
    for loc in loc_list: 
#         print(loc)
        try:
            if re.match('.*{}.*'.format(loc), text.lower()) is not None:
                if len(loc) > 4:
                    locations.append(loc)
        except:
            continue
        
#         print(locations)
    
    print('number of locations found: {}'.format(locations))
    
    x += 1
    print(x)
    return locations

            
tweet_df['location'] = tweet_df['clean_text'].apply(lambda x: matchTweet(x, loc_list))


# In[38]:


loc = 'hejhello'

re.findall('.*{}.*'.format(loc), 'hejhello, this is a tweet')


# In[21]:


def checkList(input_list):
    
    if len(input_list) > 0:
        return input_list
    else:
        return 0


# tweet_df['location'] = tweet_df['location'].apply(lambda x: checkList(x))
tweet_loc_df = tweet_df[tweet_df['location'] != 0]


tweet_loc_df


# In[22]:


tweet_loc_df.to_csv('large_file_sentiment_location.csv')

