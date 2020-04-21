# COMP560 A2 - MODEL BASED LEARNING // Sunnie Kwak
# Goal: know the policy--> calculate transition and reward
# keep track of how many times s' follows state s when you take action a
# update transition probability after you're in the new end state
# keep track of rewards after each step
# estimate U(s) with bellman's equation for U(s)

import fileinput
import random
import functions

def explore(transitions, states, data):
    data = data 
    iter = 1000 # number of iterations to record frequency
    counter = 0
    # each time record starting posit, action took, resulting state
    for i in range(iter):
        state = random.choice(states) 
        while state != "In":
            a = random.choice(list(data[state].keys())) # choose random action to take

            arr = [] # temp arr used to select result state
            for x in data[state][a].keys():  # give weight to probabilities
                num = data[state][a][x] * 100
                for i in range(int(num)):
                    arr.append(x)
            newstate = random.choice(arr) # choose state based on probabilities
            transitions[state][a].update({newstate : transitions[state][a][newstate] + 1}) # increase count of s,a,s' event

            # transition probability : s, a, s'
            # print(state + ' ' + a + ' ' + newstate)
            state = newstate
            counter = counter + 1 # total number of runs
    print(transitions)
    print(counter)

def __main__():
    data = functions.accept_input()  # initialize the dictionary with values from the .txt input
    states = functions.get_states(data)  # states is a list
    transitions = functions.transition_table_init() # dict that will store counts of each s,a,s' occurence 
    explore(transitions, states, data)
    

if __name__ == '__main__':
    __main__()