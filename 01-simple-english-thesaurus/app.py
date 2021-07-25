import json

data = json.load(open("resources/data.json"))

def get_meaning(w):    
    if w in data:
        return data[w]
    else:
        return "No such word exists. Please enter a valid word."

word = input("Enter word: ")
print(get_meaning(word))