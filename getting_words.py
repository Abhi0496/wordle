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
    
def startswith_voi(data):
    arr = []

    for word in data:
        if word["word"].startswith("voi"):
            arr.append(word["word"])
    
    return arr

def startswith_bro(data):
    arr = []
    for word in data:
        if word['word'].startswith("bro"):
            arr.append(word['word'])
    return arr

def contains_it(data):
    arr = []
    """
    temp = ["a","u","d","o","n","r","b"]
    for word in data:
        if "it" in word["word"]:
            for i in temp:
                if i in word["word"]:
                    break
            else:
                arr.append(word["word"])
    """
    for word in data:
        if word['word'].endswith('ithe'):
            arr.append(word["word"])
    return arr

def endswith_et(data):
    arr = []
    for word in data:
        if word['word'].endswith('et'):
            arr.append(word['word'])
    
    return arr

def endswith_iae(data):
    arr = []
    for word in data:
        if word["word"][1:3] == "ai" and word["word"][-1] == "e":
            arr.append(word['word'])
    
    return arr

def contains_oly(data):
    arr = []
    for word in data:
        if word["word"][1:3] == "ol" and word["word"][-1] == "y":
            arr.append(word["word"])
    
    return arr

def contains_oer(data):
    arr = []
    for word in data:
        if word["word"][1] =="o" and word["word"][3:5] == "er":
            arr.append(word["word"])
    
    for word in arr:
        temp = ['l','u','i','t','n','c','d','j','k','s']
        for j in temp:
            if j in word:
                arr.remove(word)
    return arr

def endswith_apid(data):
    arr = []

    for word in data:
        if word['word'].endswith("apid"):
            arr.append(word['word'])
    
    return arr
    
def endswith_rune(data):
    arr = []

    for word in data:
        if word['word'].endswith("rune"):
            arr.append(word['word'])
    
    return arr

if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    
    #print(endswith_ait(data))
    #print(inc(data))
    #print(startswith_voi(data))
    #print(startswith_bro(data))
    #print(contains_it(data))
    #print(endswith_et(data))
    #print(endswith_iae(data))
    #print(contains_oly(data))
    #print(contains_oer(data))
    #print(endswith_apid(data))
    print(endswith_rune(data))
else:
    print(f"Error: {response.status_code}")