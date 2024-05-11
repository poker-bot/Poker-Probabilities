# pocket_hand_analysis.py
# Aidan Nachi
# 2024.5.10
# 
# This file uses the Pandas library to build a data frame of 
# winning %s for games in varying amount of players. This
# data frame is then converted to a csv file to visualize.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict
from hand_type import Hand_type
from hold_em import Hold_em


# Go through every possible pocket cards combo and record the winning %
# for games with varrying amounts of other players.

hand_type_finder = Hand_type()
poker_simulation = Hold_em()

# Create our data frame for winning % data.
hands_df = pd.DataFrame(columns=['Pocket Cards', 'Pair', 'Connected', 
                                 'Win % 8', 'Win % 7', 'Win % 6', 'Win % 5', 
                                 'Win % 4', 'Win % 3', 'Win % 2', 'Win % 1'
                                 ])

 


# Set up the simulation with the deck, hand combos, and the amount of games
# simulated.
pocket_deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))
hand_combinations = list(itertools.combinations(pocket_deck, 2))
num_of_folding_players = 0
game_simulations = 1000

# Choose random hands when simulating.
np.random.shuffle(hand_combinations)

# Simulate games.
for hand in hand_combinations:
    hand_dict = {'Pocket Cards': hand, 
                 'Pair': hand_type_finder.is_pocket_pair(hand), 
                 'Suited': hand_type_finder.is_suited(hand), 
                 'Connected': hand_type_finder.is_connected(hand)
                 }
    
    for i in range(1, 9):
        hand_dict['Win % ' + str(i)] = poker_simulation.play_game(hand, i, game_simulations, num_of_folding_players)
    hands_df = hands_df.append(hand_dict, ignore_index=True)


# Store data frame of simulated games in a csv.






