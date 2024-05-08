import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import random
import requests
import json

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Tokenization and preprocessing functions
def tokenize(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in string.punctuation]
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

# Function to get book recommendations based on user input from the Google Books API
def get_book_recommendations(user_input):
    # API endpoint URL for Google Books API
    api_url = "https://www.googleapis.com/books/v1/volumes"
    
    # Parameters for the API request
    params = {
        'q': user_input,  # User input as the query parameter
        'maxResults': 2,   # Retrieve two results
        'orderBy': 'relevance'  # Order results by relevance
    }
    
    # Make a GET request to the Google Books API
    response = requests.get(api_url, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract book information from the response
        recommendations = []
        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', 'Unknown Title')
            authors = volume_info.get('authors', ['Unknown Author'])
            pageCount = volume_info.get('pageCount', 'Unknown')
            publishedDate = volume_info.get('publishedDate', 'Unknown')
            
            recommendation = {'title': title, 'author': ', '.join(authors), 'pageCount': pageCount, 'publishedDate': publishedDate}
            recommendations.append(recommendation)
        
        return recommendations
    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code)
        return None

# Function to generate response with detailed book information
def generate_response(user_input):
    # Tokenize user input
    tokens = tokenize(user_input)
    
    # Perform search for relevant books
    recommendations = get_book_recommendations(user_input)
    
    if recommendations:
        # Select a random book recommendation
        recommendation = random.choice(recommendations)
        
        # Construct response with book details
        response = f"I recommend '{recommendation['title']}' by {recommendation['author']}."
        
        # Add additional details about the book
        response += f"\nNumber of Pages: {recommendation.get('pageCount', 'Unknown')}"
        response += f"\nPublication Date: {recommendation.get('publishedDate', 'Unknown')}"
        
        return response
    else:
        return "I'm sorry, I couldn't find any recommendations based on your input."

# Main function to interact with the chatbot
def main():
    print("Welcome to the Book Recommendation Chatbot!")
    print("I can help you discover new books based on your interests.")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Goodbye! Have a great day!")
            break
        
        # Generate response based on user input
        response = generate_response(user_input)
        
        print("Chatbot:", response)

# Run the main function
if __name__ == "__main__":
    main()
