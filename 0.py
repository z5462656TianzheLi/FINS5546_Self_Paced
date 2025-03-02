# import libraries
import pandas as pd
import numpy as np
import nltk
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from tqdm import tqdm
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

tqdm.pandas()

export_path = r'C:\Users\samle\OneDrive\Desktop\《Machine Learning in Algo-Trading》'

# Run this line the first time you use this script and then delete it.
#nltk.download('all')

# Load the amazon review dataset
df = pd.read_csv('https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/amazon.csv')

# create preprocess_text function
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text

# apply the function df
df['reviewText'] = df['reviewText'].progress_apply(preprocess_text)

# Count the most common words in the entire 'reviewText' column
def basic_preprocess_text(text):
    tokens = text.lower().split()
    tokens = [word for word in tokens if word.isalpha()]
    return tokens

all_reviews = df['reviewText'].astype(str)
all_text = ' '.join(all_reviews)

# Preprocess the reviews
all_tokens = basic_preprocess_text(all_text)
# Count the most common words
all_word_counts = Counter(all_tokens)
# Create a dataframe for the word counts
all_df = pd.DataFrame(all_word_counts.most_common(500), columns=['Word', 'Count'])
# Display the dataframe
print(all_df)
# initialize NLTK sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# create get_sentiment function
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores['pos'] > 0 else 0
    return sentiment

# apply get_sentiment function
df['sentiment'] = df['reviewText'].apply(get_sentiment)

# Stage 3: Word Cloud #
# Separate the df into positive and negative sentiments
positive_reviews = df[df['sentiment'] == 1]['reviewText']
negative_reviews = df[df['sentiment'] == 0]['reviewText']

# Join all the reviews into a single string
positive_text = ' '.join(positive_reviews)
positive_text = word_tokenize(positive_text)
negative_text = ' '.join(negative_reviews)
negative_text =  word_tokenize(negative_text)

# Get +ve / -ve words #
sid = SentimentIntensityAnalyzer()
pos_word_list=[]

for word in positive_text:
    print(word)
    if (sid.polarity_scores(word)['compound']) >= 0.1:
        pos_word_list.append(word)

neg_word_list=[]

for word in negative_text:
    print(word)
    if (sid.polarity_scores(word)['compound']) <= -0.1:
        neg_word_list.append(word)


print('Positive:',pos_word_list)
print('Negative:',neg_word_list)

# Generate word clouds
wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(' '.join(pos_word_list))
wordcloud_negative = WordCloud(width=800, height=400, background_color='white').generate(' '.join(neg_word_list))

# Plot the word clouds
plt.figure(figsize=(20, 10))

# Positive sentiment word cloud
plt.subplot(1, 2, 1)
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.title('Positive Sentiment', fontsize=24)
plt.axis('off')

# Negative sentiment word cloud
plt.subplot(1, 2, 2)
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.title('Negative Sentiment', fontsize=24)
plt.axis('off')

# Save the figure
filename = 'word_cloud_amazon.png'
plt.savefig(os.path.join(export_path, filename))

plt.show()

# Evaluation of the Model #
print(confusion_matrix(df['Positive'], df['sentiment']))

## True Negative  --- False Positive #
## False Negative --- True  Positive #

print(classification_report(df['Positive'], df['sentiment']))
#################### END ################