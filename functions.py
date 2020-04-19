import fileinput

# formula for updating Q values in Q table:
#         q_table[state, action] = q_table[state, action] * (1 - learning_rate) + \
#             learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))
# np is the numpy library imported as: import numpy as np

# formula for updating the explore rate over time:
# exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * \
#         np.exp(-exploration_decay_rate * episode)


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
