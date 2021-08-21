import boto3
from pathlib import Path

client = boto3.client('comprehend')

oms_text = Path('temp_words.txt').read_text()

response = client.detect_sentiment(
    Text=oms_text,
    LanguageCode='en'
)
print(response)