#Get the sum of all numbers in a JSON document.

import json, re

#I wish I could instead set this as input, but it seems that VSCode has an input limit that I don't quite know my way around.
#Coming back on this, it seems that the answer involved a JSON file all along. There was no need to worry about input.
jsonDoc = open("JSONDocument.json", 'r')
#Using Regex to find all digits and the negative symbol, merging the consecuitive digits together, and summing them up.
print(sum(map(int, re.findall(r'[-0-9]+', str(json.load(jsonDoc))))))