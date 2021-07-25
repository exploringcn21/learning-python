import json

data = json.load(open('resources/data.json'))

def get_meaning(w):    
    return data[w]

word = input('Enter word: ')
print(get_meaning(word))