# Restful.py - Simple Command-Line REST Client

`restful.py` is a simple command-line REST client written in Python 3 that interacts with the JSONPlaceholder API. It allows you to make GET and POST requests to different endpoints.

## Usage

### GET Request

To make a GET request, provide the API endpoint as the argument:

./restful.py /posts

### GET request, display response
./restful.py get /posts/1

### GET request, save response to JSON file
./restful.py get /posts/1 -o output.json

### GET request, save response to CSV file
./restful.py get /posts/1 -o output.csv

### POST request, display response
./restful.py post /posts -o output.json

### POST request, save response to JSON file
./restful.py post /posts -o output.json
