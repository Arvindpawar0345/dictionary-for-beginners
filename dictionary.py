import json
from difflib import get_close_matches
data= json.load(open("original.json"))
def arvind(word):
    word=word.lower()
    if word in data:
        print(data[word])
    elif word.title() in word:
        print(data[word.title()])
    elif word.lower() in data:
        print(data[word.lower()])
    elif word.upper() in data:
        print(data[word.upper()])
    elif len(get_close_matches(word,data.keys()))>0:
        print("You mean %s "%get_close_matches(word,data.keys()))
        decide=input('Enter y or n: ')
        if decide=='y':
            aa=get_close_matches(word,data.keys())[0]
            print(aa)
            if aa in data:
                print(data[aa])
        else:
            print('Opps! Please enter valid input')
word=input('Enter your word: ')
output=arvind(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
