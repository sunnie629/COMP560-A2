# COMP560 A2 - MODEL BASED LEARNING // Sunnie Kwak
# Goal: know the policy--> calculate transition and reward
# keep track of how many times s' follows state s when you take action a
# update transition probability after you're in the new end state
# keep track of rewards after each step
# estimate U(s) with bellman's equation for U(s)

import fileinput
import random
import functions

def explore(transitions, transition_prob, state, data): # each time record starting posit, action took, resulting state
    a = random.choice(list(data[state].keys())) # choose random action to take; State is given

    arr = [] # temp arr used to select resulting state
    for x in data[state][a].keys():  # give weight to probabilities
        num = data[state][a][x] * 100
        for i in range(int(num)):
            arr.append(x)
    newstate = random.choice(arr) # choose state based on probabilities
    
    transitions[state][a].update({newstate : transitions[state][a][newstate] + 1}) # increase frequency of s,a,s'
    # transition probability : s, a, s'
    #print(state + ' ' + a + ' ' + newstate)

    # converting frequencies to transition probabilities
    reltotal = 0
    for x in transitions[state][a].keys():
        reltotal = reltotal + transitions[state][a][x]
    if reltotal != 0:
        for x in transitions[state][a].keys():
            transition_prob[state][a][x] = transitions[state][a][x]/reltotal

    # update utility
    # get_utility(s, ac, x)
    return newstate
    

# TODO: exploitation
def exploit(transitions, transition_prob, state, data, utilities):
    # get utility 
    a = get_utility(state, transition_prob, utilities)
    # choose action w min utility
    arr = [] # temp arr used to select resulting state
    for x in data[state][a].keys():  # give weight to probabilities
        num = data[state][a][x] * 100
        for i in range(int(num)):
            arr.append(x)
    newstate = random.choice(arr) # choose state based on probabilities
     
    transitions[state][a].update({newstate : transitions[state][a][newstate] + 1}) # increase frequency of s,a,s'
    # transition probability : s, a, s'
    #print(state + ' ' + a + ' ' + newstate)

    # converting frequencies to transition probabilities
    reltotal = 0
    for x in transitions[state][a].keys():
        reltotal = reltotal + transitions[state][a][x]
    if reltotal != 0:
        for x in transitions[state][a].keys():
            transition_prob[state][a][x] = transitions[state][a][x]/reltotal
    return newstate

#TODO: figure out equation for utility and picking best policy
def get_utility(state, transition_prob, utilities):
    #utilities = {}
    reward = 1
    discountval = .9 # 0 - immediate reward / 1 - later reward /// diminished reward over time
    # Bellman's equation for estimating utility: U(s) = R(s) + (discountval * max(sum(transitionprob(s,a,s') * U(s')))
    sum = 0 # sum over s'
    actionsums = {}
    for a in transition_prob[state].keys():
        for ns in transition_prob[state][a].keys():
            sum = sum + transition_prob[state][a][ns] * utilities[ns]
        actionsums.update({a : sum})
    print(actionsums)
    sum = min(actionsums.values())
    print(sum)
    action = ""
    for a in actionsums.keys():
        if actionsums[a] == sum:
            action = a
    utilities[state] = reward + (discountval * (sum))
    print(utilities)
    return a

def get_policy():
    # backpropogate to get policy
    policy = {} # dict of state : action that will be returned at the end
    pass

def __main__():
    data = functions.accept_input()  # initialize the dictionary with values from the .txt input
    transition_prob = functions.transition_table_init() # dict that will store the transition prob P(s'|s,a)
    transitions = functions.transition_table_init() # helper dictionary to store frequencies (not probabilties)
    utilities = functions.utility_table_init()

    epsilon = 1 # explore rate  
    explore_decay_rate = .02
    for i in range(100):
        state = "Fairway"
        while state != "In":
            if random.uniform(0, 1) < epsilon:
                state = explore(transitions, transition_prob, state, data)
            else:
                state = exploit(transitions, transition_prob, state, data, utilities)
            epsilon = epsilon - explore_decay_rate
        #print(transitions)
    #print(transition_prob)
            
   
    

if __name__ == '__main__':
    __main__()