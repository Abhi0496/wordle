import requests
import re
# Set the URL for the JSON file
url = "https://www.wordgamedictionary.com/word-lists/5-letter-words/get.json"

# Send a GET request to the URL
response = requests.get(url)


#Function to check words ending with ait
def endswith_ait(data):
    
    # Print the list of 5-letter words
    arr = []
    for word in data:
        if word["word"].endswith("ait"):
            arr.append(word["word"])

    return arr
            
# Check if the request was successful

def inc(data):
    arr = []
    pattern = r'(_i[nc]?[nc]?[c_]?)'
    for word_dict in data:
        word = word_dict["word"]
        if re.match(pattern, word):
            arr.append(word)
    return arr
    

if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    
    #print(endswith_ait(data))
    print(inc(data))

    
else:
    print(f"Error: {response.status_code}")