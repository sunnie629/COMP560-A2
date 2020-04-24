# COMP560 A2 - MODEL FREE LEARNING // Sunnie Kwak, Jacob Gersfeld, Kinsey Ness
# record each time starting posit, action took, and # of strokes to finish hole
# Goal: learn the utility values
# Q values tell us the value of doing action a in state s
# get Utility values by taking max Q value given state0 and action ==> U(s) = max Q(s,a)

# Bellman's equation for Q-value differs from Bellman's equation for utility values
# R(s, a) ==> gives positive/negative value for reaching a certain state

# Equation: U(s') = max Q(s, a)
# U(s) = reward * discount
# U(s) = R(s) + discountval * min(sum(P(s'|s,a)  * U(s')))


import functions
import random
import numpy as np


def do_step(data, states, actions, q, lr, discount, epsilon):

    curr_state = "Fairway"  # start state. maybe use a function to get it
    terminal_state = "In"  # end state. also maybe use a function to get it
    score = 0
    i = 1

    while curr_state != terminal_state:  # step until terminal state is reached.
        if random.uniform(0, 1) < epsilon:
            curr_action = explore(data, curr_state)
        else:
            curr_action = exploit(data, states, actions, q, curr_state)

        next_state_dict = data[curr_state][curr_action]  # ==> return dictionary
        next_state_list = list(next_state_dict.keys())
        probs = functions.generate_pdf(next_state_dict)

        # use list of probabilities to find the next state s'
        next_state = next_state_list[np.random.choice(len(next_state_dict), 1, p=probs)[0]]
        curr_reward = functions.get_reward(next_state, i)
        score += curr_reward
        i += 1

        # define indices to update proper value in Q table
        state_index = states.index(curr_state)
        action_index = actions.index(curr_action)

        # update Q value
        next_state_index = states.index(next_state)
        q[state_index, action_index] = q[state_index, action_index] * (1 - lr) + \
            lr * (curr_reward + discount * np.max(q[next_state_index, :]))

        curr_state = next_state


def explore(data, curr_state):
    random_actions_available = list(data[curr_state].keys())  # will return all actions available to this state.
    random_action = random_actions_available[random.randint(0, len(random_actions_available)-1)]
    return random_action


def exploit(data, states, actions, q, curr_state):  # pick action with max q val (max utility)
    state_index = states.index(curr_state)
    action_index = np.where(q == np.max(q[state_index, :]))
    if len(action_index[1]) > 6:
        random_actions_available = list(data[curr_state].keys())  # will return all actions available to this state.
        curr_action = random_actions_available[random.randint(0, len(random_actions_available)-1)]
    elif len(action_index[1]) > 1:
        curr_action = actions[action_index[1][random.randint(0, len(action_index[1])-1)]]
    else:
        curr_action = actions[action_index[1][0]]
    return curr_action


def __main__():

    data = functions.accept_input()  # initialize the dictionary with values from the .txt input
    states = functions.get_states(data)  # states is a list
    actions = functions.get_actions(data, states)  # actions is a set
    q = functions.create_q_table(len(states), len(actions))  # q is a q_table, used for reinforcement learning

    # next, the agent needs to interact with the environment. Either through exploration or exploitation
    # set an epsilon value: if greater than, exploit. If less than, explore.

    epsilon = 1.0  # epsilon denotes the explore rate
    max_exploration_rate = 1.0
    min_exploration_rate = .01
    exploration_decay_rate = .0001
    lr = 0.1  # how much Q will change at each iteration
    discount = .1  # set an initial discount value. "how much we weigh future trials in Q learning" close2zer=immediate

    #  10000 episodes to test
    for i in range(10000):
        do_step(data, states, actions, q, lr, discount, epsilon)
        epsilon = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * \
            np.exp(-exploration_decay_rate * i)

    functions.print_mf_policy(q, data, states, actions)
    print()
    functions.print_mf_utilities(q, data, states, actions)

    # step 1: use epsilon to choose explore vs exploit
    # step 2: choose start state (randomly?)
    # step 3: if explore, choose random action, use probabilities to go to next state. start a score?
    # step 4: continue until end state is reached. Compute scores once end state reached
    # step 5: update Q table using reward, gamma, current Q val (at matrix index), and learning rate


if __name__ == '__main__':
    __main__()
