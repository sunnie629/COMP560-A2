import fileinput
import numpy as np

# formula for updating Q values in Q table:
#         q_table[state, action] = q_table[state, action] * (1 - learning_rate) + \
#             learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))

# formula for updating the explore rate over time:
# exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * \
#         np.exp(-exploration_decay_rate * episode)


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
    # if state == "Ravine":
    #     return 0/count
    # elif state == "Over":
    #     return 0/count
    # elif state == "Same":
    #     return 0/count
    # elif state == "Left":
    #     return 0/count
    if state == "Close":
        return 0.5/count
    elif state == "In":
        return 1/count
    else:
        return 0
    pass


def get_states(data):
    states = []
    for key in data.keys():
        states.append(key)
    return states


def get_actions(data, states):
    actions = set()
    for state in states:
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
