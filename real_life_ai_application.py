# Install the TextBlob library if you don't have it
# !pip install textblob

from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity: -1 (negative) to 1 (positive)
    sentiment = blob.sentiment.polarity
    
    # Print the result
    if sentiment > 0:
        print("The sentiment of the text is Positive.")
    elif sentiment < 0:
        print("The sentiment of the text is Negative.")
    else:
        print("The sentiment of the text is Neutral.")

# Example texts
text1 = "I love this product, it works great!"
text2 = "I hate waiting in long lines at the store."
text3 = "The weather is okay today."

# Analyze sentiment of each text
analyze_sentiment(text1)
analyze_sentiment(text2)
analyze_sentiment(text3)
