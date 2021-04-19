import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())):
        print("closest match is",get_close_matches(word,data.keys())[0])
        return data[get_close_matches(word,data.keys())[0]]
    else:
        return ["word not found"]

word=input("Enter a word to be found in dictionary ")
word.lower()

print(*translate(word),sep='\n')
