import json
import difflib

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    # ratio1 = difflib.SequenceMatcher(None, w, data.keys()).ratio()
    ratio = difflib.get_close_matches(w, data.keys(), cutoff=0.8)
    # print(ratio)
    if w in data:
        return data[w]
    elif len(ratio) != 0:
        realWord = difflib.get_close_matches(w, data.keys())[0]
        yn = input("Do you mean %s instead? Enter Y for Yes and N for No. " % realWord)
        if yn == "Y":
            return data[realWord]
        else:
            return "We didn't understand your query!"
    else:
        return "The word does not exist!"

word = input("Enter the word? ")
output = (translate(word))
if type(output) == list:
    for item in output:
        print(item)
else :
    print(output)
