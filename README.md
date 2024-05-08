# CSC510_AIProject
Our 'Bookwise' script leverages Google Books API and the Natural Language Toolkit to create custom recommendations based on user input.

```python
# Tokenization and preprocessing functions
def tokenize(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in string.punctuation]
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

```
