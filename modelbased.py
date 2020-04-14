# COMP560 A2 - MODEL BASED LEARNING // Sunnie Kwak
import fileinput
import random

file_ = fileinput.input() # reading file from STDIN

states = {} # dict of {s: {a : {s' : prob}}}
start = True
state = ""
action = ""
actions = {}

for x in file_:
    word = x.split('/') 
    states[word[0]] = {}

file_ = fileinput.input()
for x in file_:
    word = x.split('/') 
    if start:
        state = word[0]
        action = word[1]
        states[word[0]].update({word[1]: {} })
        start = False
    if word[0] == state:
        if word[1] == action:
            states[word[0]][word[1]].update({word[2] : float(word[3].rstrip())})
        else:
            action = word[1]
            states[word[0]].update({word[1]: {} })
            states[word[0]][word[1]].update({word[2] : float(word[3].rstrip())})
    else:
        state = word[0]
        action = word[1]
        states[word[0]].update({word[1]: {} })
        states[word[0]][word[1]].update({word[2] : float(word[3].rstrip())})
state = "Fairway"

while state != "In":
    a = random.choice(list(states[state].keys())) # choose random action to take
    arr = []
    
    for x in states[state][a].keys(): # give weight to probabilities
        num = states[state][a][x] * 100
        for i in range(int(num)):
            arr.append(x)
    state = random.choice(arr)
    break
    #(list(states[state][a].keys()))
    
    