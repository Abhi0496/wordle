I was solving wordle and found the last three words which were "ait"
I had only 2 chances left and wanted to solve it badly.

So I created two python file
1) wordle.py-
    My initial idea was to find all the words ending with "ait", doesn't really matters if its a word or not.
I thought there will be max 52 words and then I would traverse through all of them to find out the most appropriate word.
But soon I found out that its too taxing which lead to the creation of getting_words.py

2) getting_words.py-
    Here I used "requests" python library to fetch a JSON file which contains all the 5 letters (meaningful) words.
Found the url that can give me those words. Then Filtered the list to include only the words ending with "ait".
Then printed those words. Here unlike my wordle.py file, the words I got were very few hence it became easy to find the correct word.
