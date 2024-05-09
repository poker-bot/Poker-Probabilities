# hold_em.py
# Aidan Nachi
# 2024.5.8
#
# This file defines a class that simulates a game of texas holdem.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

from win_finder import Win_finder


class hold_em():
    """ Implement a game of Texas Hold'em. """

    def __init__(self):
        """ Initialize a game of Texas Hold'em. """

        # Create a deck of playing cards. 
        # Deck key
        # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace
        self.deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))

    
    def holdem_simulation(self, players_hand, num_other_players, num_of_folding_players=0):
        """ Simulate a game of Texas Hold'em. """

        # Copy deck for playing.
        playing_deck = self.deck.copy()

        # Shuffle our deck.
        np.random.shuffle(playing_deck)

        # Remove player's hand from playing deck.
        playing_deck = list(filter(lambda x: x != players_hand[0], playing_deck))
        playing_deck = list(filter(lambda x: x != players_hand[1], playing_deck))

        # Create the other players in the game.
        other_players_hands = []
        for i in range(num_other_players):
            other_players_hands.append([playing_deck.pop(0), playing_deck.pop(0)])

        # Game Play
        # Simulate flop, turn, and river.
        #--------------------------------
        flop = playing_deck[0:4]

        # Burn the card that was at the top of the deck. 
        del playing_deck[0:4]

        # Turn and burn the first two cards in the deck.
        turn = playing_deck[0:2]
        del turn[0]

        # Lay down the second two cards of the river.
        river = playing_deck[0:2]
        del playing_deck[0:2]

        # Burn a card from the river.
        del river[0]

        # The board is the sum of the flop (3 cards), the turn (1 card), and the river (1 card).
        board = flop + turn + river

        # Handle folding of other players if set. 
        if num_of_folding_players > 0 and num_of_folding_players < num_other_players:

            # Incorporate the randomness of folding.
            folding_players = np.random.randint(1, num_other_players, num_of_folding_players)
            hands_to_delete = []

            for num in folding_players:
                hands_to_delete.append(other_players_hands)
            
            # Filter out the hand of the folding player from the other players.
            for hand in hands_to_delete:
                other_players_hands = list(filter(lambda x: x != hand, other_players_hands))

        # Find the winning hand.
        win_finder = Win_finder()
        return win_finder.game_result(players_hand, other_players_hands, board)

        

