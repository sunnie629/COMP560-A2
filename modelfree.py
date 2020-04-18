# COMP560 A2 - MODEL FREE LEARNING // Sunnie Kwak
# record each time starting posit, action took, and # of strokes to finish hole
import fileinput
import functions
import gym


def __main__():

    states = functions.accept_input()
    print(states["Fairway"].keys())
    print(states.keys())
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

