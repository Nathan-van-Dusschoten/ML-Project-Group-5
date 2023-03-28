from tock import make
from random import choice


def random_player(obs, info):
    """
    defines a random player: returns a random action from the actionspace
    """
    action = choice(info['space'])
    return action 


# create an instance of the game with 6 players
env = make(nplayers=6, render=True)

# reset the game
obs, rew, done, info = env.reset()

while True:
    # get an action from the random player
    action = random_player(obs, info)

    # pass the action and get the new gamestate
    obs, rew, done, info = env.step(action)

    # render for graphical representation of gamestate
    env.render()

    # quit if game is finished
    if done:
        break
