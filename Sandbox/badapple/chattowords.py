import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


chat_df = pd.read_csv("C:\Code\Python3\Sandbox#py\chat_analysis"
                      "\chat_history 2024-02-16.csv")

tokens = []
for m in chat_df[~chat_df.text.str.startswith('File: <')].text:
    if 'http://' in m or 'https://' in m:
        pattern = (r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]'
                   r'|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        # links = re.findall(pattern, m)
        m = re.sub(pattern, '', m)
    
    tokens.append(word_tokenize(m, language='russian'))

lowercase_tokens = [[token.lower() for token in m] for m in tokens]

stop_words = set(stopwords.words('russian'))
filtered_tokens = [[word for word in m if word not in stop_words] for m
                   in lowercase_tokens]

# print([word for word in m for m in filtered_tokens for word in m])
tokenized_words = list(filter(lambda x: x, [
    re.sub(r'[^a-zA-Zа-яёА-ЯЁ@#\s]', '', word)
    for m in filtered_tokens
    for word in m]))

with open('chat_text.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(tokenized_words))
