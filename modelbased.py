# COMP560 A2 - MODEL BASED LEARNING // Sunnie Kwak
# Goal: know the policy--> calculate transition and reward
# keep track of how many times s' follows state s when you take action a
# update transition probability after you're in the new end state
# keep track of rewards after each step
# estimate U(s) with bellman's equation for U(s)

import fileinput
import random
import functions

def explore(transition_prob, states, data):
    data = data 
    iter = 500 # number of iterations to record frequency; higher - more accurate
    counter = 0
    reward = 1 # 
    transitions = functions.transition_table_init()

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
            
            transitions[state][a].update({newstate : transitions[state][a][newstate] + 1}) # increase frequency of s,a,s'
            # transition probability : s, a, s'
            # print(state + ' ' + a + ' ' + newstate)
            state = newstate
            counter = counter + 1 # total number of runs
    
    # converting frequencies to transition probabilities
    for s in transitions.keys():
        for ac in transitions[s].keys():
            reltotal = 0
            for x in transitions[s][ac].keys():
                reltotal = reltotal + transitions[s][ac][x]
            if reltotal != 0:
                for x in transitions[s][ac].keys():
                    transition_prob[s][ac][x] = transitions[s][ac][x]/reltotal
    print(transitions)
    print(transition_prob)
    print(counter)

  # TODO: exploitation
def exploit():
    pass

def __main__():
    data = functions.accept_input()  # initialize the dictionary with values from the .txt input
    states = functions.get_states(data)  # states is a list
    transition_prob = functions.transition_table_init() # dict that will store the transition prob P(s'|s,a)
    
    # TODO: Add epsilon and discount value functionality
  
    discountval = 0 # 0 - immediate reward / 1 - later reward
    epsilon = 0 # explore rate  
    
    explore(transition_prob, states, data)
    

if __name__ == '__main__':
    __main__()