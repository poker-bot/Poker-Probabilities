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


class Hold_em():
    """ Implement a game of Texas Hold'em. """

    def __init__(self):
        """ Initialize a game of Texas Hold'em. """

        # Create two alternating decks of playing cards. 
        # Deck key
        # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace
        self.deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))
        self.second_deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))

    
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
    

    def holdem_simulation_winning_hand(self, num_of_players):
        """ Simulate a game of Texas Holdem and get the winning hand. """

        # Make a copy and shuffle the deck to play.
        second_playing_deck = self.second_deck.copy()
        np.random.shuffle(second_playing_deck)

        # Create players to and deal them hole cards so we can find the winner.
        players_hands = []
        for i in range(num_of_players):
            players_hands.append([second_playing_deck.pop(0), second_playing_deck.pop(0)])


        # Simulate the flop, turn, and river to get the board.
        # ----------------------------------------------------
        # Take 4 cards from the top of the deck, burn one and flip three.
        flop = second_playing_deck[0:4]
        del second_playing_deck[0:4]
        del flop[0]
        
        # Take two cards from the top of the deck, burn and turn the
        # turn card (fourth community card).
        turn = second_playing_deck[0:2]
        del second_playing_deck[0:2]
        del turn[0]

        # Take two cards from the top of the deck, then burn one and turn
        # the river card (last community card).
        river = second_playing_deck[0:2]
        del second_playing_deck[0:2]
        del river[0]

        # The sum of cards from the flop, turn, and river make up the board.
        board = flop + turn + river


        # Return the winning hand of the game simulation.
        win_finder = Win_finder()
        return win_finder.winning_result(players_hands, board)
    

    def play_game(self, players_hand, num_of_other_players, game_sims, num_of_folding_players):
        """ Play a game of Texas Hold'em. 
        
        Calculate the win percentages of certain hands. 
        """

        wins = 0

        # Play games through numerous simulations.
        for i in range(game_sims):
            result = self.holdem_simulation(players_hand, num_of_other_players, num_of_folding_players)

            # Count wins and ties as wins since you split the pot and always end
            # up with more chips in a tie scenario.
            if result == 'Win' or result == 'Tie':
                wins += 1

            win_percentage = (wins / game_sims) * 100

            return win_percentage






        

