# COMP560 A2 - MODEL FREE LEARNING // Sunnie Kwak
# record each time starting posit, action took, and # of strokes to finish hole
import functions
import gym


def __main__():
    data = functions.accept_input()  # initialize the dictionary with values from the .txt input
    states = functions.get_states(data)  # states is a list
    actions = functions.get_actions(data, states)  # actions is a set
    q = functions.create_q_table(len(states), len(actions))  # q is a q_table, used for reinforcement learning

    print(states)
    print(actions)

    # TODO: next, the agent needs to interact with the environment. Either through exploration or exploitation
    # TODO: code below can be copy and pasted to functions.py, once complete.
    # epsilon value can be used to balance exploration vs exploitation
    # set an epsilon value: if greater than 0.5, exploit. If less than, explore.

    # print(data["Fairway"].keys())
    # print(data.keys())

    for i in range(100):
        pass
        # step 1: use epsilon to choose explore vs exploit
        # step 2: choose start state (randomly?)
        # step 3: if explore, choose random action, use probabilities to go to next state. start a score?
        # step 4: continue until end state is reached. Compute scores once end state reached
        # step 5: update Q table using reward, gamma, current Q val (at matrix index), and learning rate


    # TODO: add in gym library function to try to create a Q table.

    # print(states)  # let's modify function so it actually works
    # print(actions)
    # env = gym.make('MsPacman-v0')
    # env.reset()
    # for _ in range(1000):
    #     env.render()
    #     env.step(env.action_space.sample()) # take a random action
    # env.close()


if __name__ == '__main__':
    __main__()
