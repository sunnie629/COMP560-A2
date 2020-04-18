import fileinput


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
