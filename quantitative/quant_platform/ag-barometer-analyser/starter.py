import requests
import xml.etree.ElementTree as ET
from textblob import TextBlob

# URL of the XML file
url = "https://ag.purdue.edu/commercialag/ageconomybarometer/category/report/feed/"

# Send a GET request to download the XML data
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)

    # Extract text from XML elements
    text = ''
    for element in root.iter():
        if element.text:
            text += element.text.strip() + ' '

    # Preprocess the text
    preprocessed_text = text.lower()  # Convert to lowercase

    # Perform sentiment analysis using TextBlob
    blob = TextBlob(preprocessed_text)
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity

    # Analyze the sentiment results
    if sentiment_polarity > 0:
        sentiment_label = 'Positive'
    elif sentiment_polarity < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    # Print the sentiment analysis results
    print('Sentiment Polarity:', sentiment_polarity)
    print('Sentiment Subjectivity:', sentiment_subjectivity)
    print('Sentiment Label:', sentiment_label)
else:
    print("Failed to download the XML file.")