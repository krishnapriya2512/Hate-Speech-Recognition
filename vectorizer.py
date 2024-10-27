from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
import re
import os
import pickle

cur_dir = os.path.dirname(__file__)
stop = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'stopwords.pkl'), 'rb'))
vect = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'vect_bog.pkl'), 'rb'))


lemmatizer = WordNetLemmatizer()

def preprocessor(tweet):
    
    # Removal of user handles
    tweet = re.sub('@[\w\-]+','', tweet)
    
    # Coverting the string into lower case
    tweet = str(tweet).lower()
    
    tweet = re.sub('\[.*?\]','',tweet)
    
    # Removal of HTML linkups
    tweet = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|''[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',tweet)
    tweet = re.sub('<.*?>+', '', tweet)
    
    # Removal of punctuations
    tweet = re.sub('[%s]' % re.escape(string.punctuation), '', tweet)
    tweet = re.sub('\n','',tweet)
    tweet = re.sub('\w*\d\w*', '', tweet)
    
    # Removal of stopwords
    tweet = [word for word in tweet.split(' ') if word not in stop]
    
    #removal of greek characters
    tweet = [' '.join([unidecode.unidecode(word) for word in str(t).split()]) if t is not None else t for t in tweet]
    
    #lemmetizing of tweets
    tweet = [" ".join(lemmatizer.lemmatize(word) for word in t.split()) for t in tweet]
    
    tweet = " ".join(tweet)
    return tweet

#vect = CountVectorizer()

def process_tweet(tweet):
    # Process the tweet
    processed_tweet = preprocessor(tweet)

    
    vect.transform([processed_tweet])  # Pass a list of processed_tweet

    return processed_tweet
