import fileinput
import numpy as np


def print_mf_policy(q, data, states, actions):
    print("Policy:")
    for state in list(data.keys()):
        state_index = states.index(state)
        action_index = np.argmax(q[state_index, :])
        print(states[state_index], "-->", actions[action_index])


def print_mf_utilities(q, data, states, actions):
    print("Utilities:")
    for state in data.keys():
        if state == "In":
            continue
        for action in data[state]:
            state_index = states.index(state)
            action_index = actions.index(action)
            q_val = q[state_index][action_index]
            for next_state in data[state][action]:
                print(state, ",", action, ",", next_state, ":", data[state][action][next_state]*q_val)


def create_q_table(states_length, actions_length):
    return np.zeros((states_length, actions_length))


def get_start_state(states):
    return states[0]


def get_terminal_state(data, states):
    pass  # return the set difference of all available start states from total states


def generate_pdf(state_probs):
    probs = []
    for key in state_probs.keys():
        probs.append(state_probs[key])
    return probs


def get_reward(state, count):

    if state == "Close":
        return 0.5/count
    elif state == "In":
        return 1/count
    else:
        return 0
    pass


def get_states(data):
    states = set()
    for key in data.keys():
        states.add(key)
        for value in data[key].values():
            for state in value.keys():
                states.add(state)

    return list(states)


def get_actions(data, states):
    actions = set()
    for state in states:
        if data.get(state) is None:
            continue
        else:
            for action in data[state].keys():
                actions.add(action)
    return list(actions)


def accept_input():
    file_ = fileinput.input()  # reading file from STDIN

    states = {} # dict of {s: {a : {s' : prob}}}
    start = True
    state = ""
    action = ""

    # file reading & set up of states dictionary
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

    return states


def transition_table_init(): # values all init to 0
    file_ = fileinput.input()  # reading file from STDIN

    states = {} # dict of {s: {a : {s' : prob}}}
    start = True
    state = ""
    action = ""

    # file reading & set up of states dictionary
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
                states[word[0]][word[1]].update({word[2] : 0})
            else:
                action = word[1]
                states[word[0]].update({word[1]: {} })
                states[word[0]][word[1]].update({word[2] : 0})
        else:
            state = word[0]
            action = word[1]
            states[word[0]].update({word[1]: {} })
            states[word[0]][word[1]].update({word[2] : 0})

    return states


def utility_table_init():
    file_ = fileinput.input()  # reading file from STDIN

    states = {}  # dict of {s: 0}

    # file reading & set up of states dictionary
    for x in file_:
        word = x.split('/')
        states[word[0]] = 0
    states.update({"In" : 1})
    return states
