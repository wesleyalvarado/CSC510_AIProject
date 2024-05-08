# CSC510_AIProject
BookWise: An AI-Powered Book Recommendation Chatbot is a project designed to assist users in discovering new books based on their interests.  BookWise utilizes the Natural Language Toolkit (NLTK) library for tokenization, preprocessing, and lemmatization of user input.  In addition, our program integrates with the Google Books API which provides access to a vast database of books, authors, and related metadata. 

As a sample of our code, below we can see the proprocessing method used to tokenize user input:


```python
def tokenize(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in string.punctuation]
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

```
