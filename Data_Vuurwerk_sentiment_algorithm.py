
# coding: utf-8

# In[ ]:

# import libraries

import pandas as pd
import nltk #Natural Language processing - Recognizes words from strings
import re #regular expression - to recognize certain patterns in text
from textblob import TextBlob #sentiment analysis - pre trained model

# df = create dataframe
df = pd.read_csv('textfile_keywords_based_unknown_location.csv')

#def = functie. Text = imput. Replaces random chacacters
def decode(text):

    text = (text.
            replace('\\xe2\\x80\\x99', "'").
            replace('\\xc3\\xa9', 'e').
            replace('\\xe2\\x80\\x90', '-').
            replace('\\xe2\\x80\\x91', '-').
            replace('\\xe2\\x80\\x92', '-').
            replace('\\xe2\\x80\\x93', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x98', "'").
            replace('\\xe2\\x80\\x9b', "'").
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9d', '"').
            replace('\\xe2\\x80\\x9e', '"').
            replace('\\xe2\\x80\\x9f', '"').
            replace('\\xe2\\x80\\xa6', '...').#
            replace('\\xe2\\x80\\xb2', "'").
            replace('\\xe2\\x80\\xb3', "'").
            replace('\\xe2\\x80\\xb4', "'").
            replace('\\xe2\\x80\\xb5', "'").
            replace('\\xe2\\x80\\xb6', "'").
            replace('\\xe2\\x80\\xb7', "'").
            replace('\\xe2\\x81\\xba', "+").
            replace('\\xe2\\x81\\xbb', "-").
            replace('\\xe2\\x81\\xbc', "=").
            replace('\\xe2\\x81\\xbd', "(").
            replace('\\xe2\\x81\\xbe', ")")
                 )
    
    text = re.sub(r'[^\x00-\x7F]+', '', text)
        
    return text


# In[ ]:
# cleantext = functie die text cleaned
def cleanText(text):
    #split de text op spaties
    text = text.split()
   
    # remove links
    text = [x for x in text if re.match('^http.*', x) is None]
    
    # remove tags
    text = [x for x in text if re.match('^#.*', x) is None]
    
    # remove @
    text = [x for x in text if re.match('^@.*', x) is None]
    
    # remove list of words
    remove_list = ["b'RT", "RT"]
    text = [x for x in text if x not in remove_list]
    
    # remove 'b
    text = [x for x in text if re.match("^b'.*", x) is None]
    
    # remove \x
    text = [x for x in text if re.match('^\\\\x.*', x) is None]
    
    # Recreate string from list. use nltk.
    text = " ".join(text)
    text = nltk.word_tokenize(text)
    
    # filter out random stuff (remove everything that are not letters)
    text = [x for x in text if re.match('\W+', x) is None]
    
    # make sure lenght is more than 1 (removes 1 letter words. Also 'a' 'I' but doesn't influence sentiment analysis
    text = [x for x in text if len(x)>0]
    
    return " ".join(text)


# In[ ]:

# sentiment analysis done with TextBlob. Check out http://textblob.readthedocs.io/en/dev/quickstart.html 
# for a description

def getSentiment(text):
    #textblob functie
    testimonial = TextBlob(text)
    #return polarity score -1 to 1
    return testimonial.sentiment.polarity


# In[ ]:

# clean text and apply to entire dataframe
#lamba betekent applies to x
df['clean_text'] = df['text'].apply(lambda x: decode(x))
df['clean_text'] = df['clean_text'].apply(lambda x: cleanText(x))

# get sentiment and apply to entire dataframe
df['sentiment'] = df['clean_text'].apply(lambda x: getSentiment(x))


# In[182]:

# make a split to only include rows 
#exclude sentiment 0. Dit weghalen als je ook sentiment 0 wilt. Dan moet je bij export new_df vervangen door df.
new_df = df[df['sentiment'] != 0]


# In[184]:

print(new_df)

# In[186]:

# export dataframe 

new_df.to_csv('small_file_sentiment.csv')

# In[ ]:



