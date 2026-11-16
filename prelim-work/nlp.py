"""
Testign various NLP Libraries: https://www.geeksforgeeks.org/nlp/nlp-libraries-in-python/ 
"""
from textblob import TextBlob

text = TextBlob("I love learning NLP with Python.")

print(text.sentiment)
