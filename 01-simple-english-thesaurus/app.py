import json
from difflib import get_close_matches

data = json.load(open("resources/data.json"))

def get_meaning(w):
    w = w.lower()    
    if w in data:
        return data[w]
    else:
        possible_words = get_close_matches(word=w, possibilities=data.keys(), cutoff=0.75)
        if len(possible_words) > 0:
            user_response = input(f"No such word exists. Did you mean '{possible_words[0]}'? Enter yes/no: ")
            if user_response.lower() == "yes":
                return data[possible_words[0]]
            elif user_response.lower() == "no":
                return "No such word exists. Please enter a valid word."
            else:
                return "Sorry. Please enter 'yes' or 'no' as a response."
        else:
            return "No such word exists. Please enter a valid word."


word = input("Enter word: ")
print(get_meaning(word))