import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from nltk import word_tokenize
from sklearn.model_selection import train_test_split
from textblob import TextBlob


# Load spaCy language model and add the TextBlob extension
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

# Read the CSV file
ReviewsTable = pd.read_csv('amazon_product_reviews.csv', low_memory=False)

# Data Cleaning remove na in the review columns
ReviewsData =  ReviewsTable.dropna(subset=['reviews.text', 'reviews.rating'])

#Split test and training samples
X = ReviewsData['reviews.text']
y = ReviewsData['reviews.rating']


review_score_map = {
    5:'Positive',
    4:'Positive',
    3:'Neutral',
    2:'Negative',
    1:'Negative'
}
ReviewsData['reviews.rating'] = y.map(review_score_map)

# Define a function to analyze sentiment of review text
def analyze_sentiment(review_text: str, threshold:0.3):
    
    # define an empty list to contain the reviews without stop words.
    reviews_without_stops = []
    for char in nlp(review_text):
        if not char.is_stop:
            reviews_without_stops.append(str(char))
    # join the lists of the words
    reviews_joined = ' '.join(reviews_without_stops)
    lower_review_ = reviews_joined.lower().strip()
    
    #Use TextBlob for sentiment analysis
    blob = TextBlob(lower_review_)
    
    # Get the sentiment polarity
    sentiment_score = blob.sentiment.polarity
    if sentiment_score == threshold : sentiment = 'Neutral'
    elif sentiment_score > threshold: sentiment = 'Positive'
    else: sentiment = 'Negative'
    return sentiment

# run the sentimental analysis on reviews and return the reviews as positive, negative or neutral
# compare the accuracy with the real review score.

def eval_score(Data_input, threshold):
    
    result_table = pd.DataFrame({'reviews.text': Data_input['reviews.text']})
    result_table['sentimental_output'] = result_table['reviews.text'].apply(lambda x: analyze_sentiment(x, threshold))
    result_table['real_score'] = ReviewsData['reviews.rating']
    print(result_table.head())

    accuracy_score = ((result_table['sentimental_output']== result_table['real_score']).sum())/len(result_table)
    return [result_table,accuracy_score]

# Below is the process to return the best threshold for sentimental score. 
# Based on the best accuracy score returned from eval_score function. 
result = eval_score(ReviewsData, 0)
print("The final accuracy of the sentimental analysis is: ",result[1])

submission = result[0]
submission.to_csv("submission_file.csv",index = False)



# #Analysis Result:
# #According to the output, we can see that There are:
# # Positive reviews: 4374,
# # Neutral reviews: 401,
# # Negative reviews: 225.
# #So most of the comments are positive.
