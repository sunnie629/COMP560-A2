# COMP560 A2 - MODEL BASED LEARNING // Sunnie Kwak
# Goal: know the policy--> calculate transition and reward
# keep track of how many times s' follows state s when you take action a
# update transition probability after you're in the new end state
# keep track of rewards after each step
# estimate U(s) with bellman's equation for U(s)

import fileinput
import random
import functions

def explore(transitions, transition_prob, state, data, utilities): 
    get_best_utility(state, transition_prob, utilities)
    a = random.choice(list(data[state].keys())) # choose random action to take based on given state 

    # following code determines s' based on probabilties
    arr = [] # helper arr used to select resulting state
    for x in data[state][a].keys():  # give weight to probabilities
        num = data[state][a][x] * 100
        for i in range(int(num)):
            arr.append(x)
    newstate = random.choice(arr) # determine new state based on probabilities

    transitions[state][a].update({newstate : transitions[state][a][newstate] + 1}) # increase frequency of s,a,s'
    # converting frequencies to transition probabilities and recording that in transition probability dict
    reltotal = 0
    for x in transitions[state][a].keys():
        reltotal = reltotal + transitions[state][a][x] 
    if reltotal != 0:
        for x in transitions[state][a].keys():
            transition_prob[state][a][x] = transitions[state][a][x]/reltotal

    return newstate

def exploit(transitions, transition_prob, state, data, utilities):
    a = get_best_utility(state, transition_prob, utilities) # choose action that minimizes the utility

    # Based on returned action, determine new state
    arr = [] # temp arr used to select resulting state
    for x in data[state][a].keys():  # give weight to probabilities
        num = data[state][a][x] * 100
        for i in range(int(num)):
            arr.append(x)
    newstate = random.choice(arr) # choose state based on probabilities

    transitions[state][a].update({newstate : transitions[state][a][newstate] + 1}) # increase frequency of s,a,s'

    # converting frequencies to transition probabilities to update transition probability table
    reltotal = 0
    for x in transitions[state][a].keys():
        reltotal = reltotal + transitions[state][a][x]
    if reltotal != 0:
        for x in transitions[state][a].keys():
            transition_prob[state][a][x] = transitions[state][a][x]/reltotal

    return newstate

def get_best_utility(state, transition_prob, utilities):
    reward = 1 # reward is fixed at 1 for each stroke
    discountval = .1 # 0 - immediate reward / 1 - later reward 

    different = True # boolean used to determine if more value iterations are needed
    actionsums = {} # holds the possible utilities for each action {a : utility val} for given state
    action = ""

    # Bellman's equation for estimating utility: U(s) = R(s) + discountval * min(sum(P(s'|s,a)  * U(s')))
    while different: # while values have not converged:
        for a in transition_prob[state].keys():
            sum = 0 
            for ns in transition_prob[state][a].keys():
                sum = sum + transition_prob[state][a][ns] * utilities[ns] # sum(P(s'|s,a) * U(s')) for action a
            actionsums.update({a : sum}) # for each action in given state, store sum(P(s'|s,a) * U(s'))
        
        sum = min(actionsums.values()) # pick the minimum value

        # determine if more value iterations are needed
        if reward + (discountval * (sum)) - .0005 <= utilities[state]:
            if reward + (discountval * (sum)) + .0005 >= utilities[state]:
                different = False # if values have converged, no more iterations 
        utilities[state] = reward + (discountval * (sum)) # set new utility value

        #print(utilities)
    #print("~~~~~~~~~~~~~")
    for a in actionsums.keys(): # this is used to get the key from minimum value (since dictionaries do not support val -> key retrieval)
        if actionsums[a] == sum: # get action of that minimum value (optimal action)
            action = a
         
    #print(actionsums)
    return action

def get_policy(state, transition_prob, utilities, data): # print optimal action to take for each state
    for s in utilities.keys():
        if s != "In":
            a = get_best_utility(s, transition_prob, utilities)
            print(s + " -> " + a)
            
   
def __main__():
    data = functions.accept_input()  # initialize the dictionary with values from the .txt input
    transition_prob = functions.transition_table_init() # dict that will store the transition prob P(s'|s,a)
    transitions = functions.transition_table_init() # helper dictionary to store frequencies (not probabilties)
    utilities = functions.utility_table_init() # dictionary to store utility values {s: U(s)}

    epsilon = 1 # explore rate
    min_exploration_rate = .01
    explore_decay_rate = .00002

    for i in range(50000):
        state = "Fairway"
        while state != "In":
            #print(state)
            if random.uniform(0, 1) < epsilon + min_exploration_rate:
                state = explore(transitions, transition_prob, state, data, utilities)
            else:
                state = exploit(transitions, transition_prob, state, data, utilities)
            epsilon = epsilon - explore_decay_rate
    #print("-----------")
    #print(utilities)
    print("-----------")
    print("Transition Probabilities for State, Action, State' :")
    for s in transition_prob.keys():
        for a in transition_prob[s].keys():
            for ns in transition_prob[s][a].keys():
                print(s + ", " + a + ", " + ns + " : " + str(transition_prob[s][a][ns]))
    print("-----------")
    print("Policy:")

    get_policy(state, transition_prob, utilities, data) # get_policy makes use of exploit function
      


if __name__ == '__main__':
    __main__()