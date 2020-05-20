import json
import random

with open('data.json') as json_file:
    tmpdict = json.load(json_file)

with open('vocabulary.json') as json_file:
    vocabulary = json.load(json_file)

random.shuffle(tmpdict["Tweets"])

charArr = []
for tweet in tmpdict["Tweets"]:
    for char in tweet:
        charArr.append(char)

nextChar = []
for i in range(len(charArr)):
    try:
        nextChar.append(charArr[i+1])
    except IndexError:
        nextChar.append(" ")


def encode(character,vocabulary):
    vocabArr = []
    for key in vocabulary:
        if character == key:
            vocabArr.append(1)
        else:
            vocabArr.append(0)
    
    return vocabArr

def decode(array,vocabulary):
    i = 0
    for key in vocabulary:
        if array[i] == 1:
            return key
        i+=1

datasetDict = {}
for i in range(len(charArr)):
    inArr = encode(charArr[i],vocabulary)
    outArr = encode(nextChar[i],vocabulary)
    datasetDict[f"{i}"] = [inArr,outArr]

print(datasetDict["0"])


with open("dataset.json","w") as json_file:
    json.dump(datasetDict,json_file)

