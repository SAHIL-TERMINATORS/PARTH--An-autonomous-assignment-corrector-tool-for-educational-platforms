import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon and initialize the sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Sample text extracted from the PDF
pdf_text = "I absolutely hate this book! The characters were amazing and the plot kept me engaged."

# Perform sentiment analysis using VADER
sentiment_scores = sia.polarity_scores(pdf_text)

# Determine sentiment based on the compound score
if sentiment_scores['compound'] > 0.05:
    sentiment = "Positive"
elif sentiment_scores['compound'] < -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")
print(f"Positive: {sentiment_scores['pos']:.2f}, Negative: {sentiment_scores['neg']:.2f}, Neutral: {sentiment_scores['neu']:.2f}")
