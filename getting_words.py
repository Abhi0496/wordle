import requests
# Set the URL for the JSON file
url = "https://www.wordgamedictionary.com/word-lists/5-letter-words/get.json"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful

if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    #print(data)

    
    # Print the list of 5-letter words
    arr = []
    for word in data:
        if word["word"].endswith("ait"):
            arr.append(word["word"])

    print(arr)
        #print(word["word"])
else:
    print(f"Error: {response.status_code}")