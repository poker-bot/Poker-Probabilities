# hand_type_finder.py
# Aidan Nachi
# 2025.5.10
# 
# This file defines a class that detects and generates certain hand types.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict


class hand_type():
    """ Implement a hand type detector and generator. """

    def __init__(self):
        """ Initialize a hand type class. """

        # Create a deck of playing cards. 
        # Deck key
        # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace
        self.deck =  list(itertools.product(range(2,15),['Spade','Heart','Diamond','Club']))

    def is_pocket_pair(self, cards):
        """ Detect a pocket pair. """

        # Check if rank of cards are both the same.
        if cards[0][0] == cards[1][0]:
            return True
        else:
            return False
        
    
    def is_suited(self, cards):
        """ Detect if the hand is suited. """

        # Check if the suit of both cards are the same.
        if cards[0][1] == cards[1][1]:
            return True
        else:
            return False
        

    def is_connected(self, cards):
        """ Detect if the cards are connected. """

        # Check if the card values are consecutive (ex: 1,2 or 8,7)
        if (cards[0][0] + 1) == cards[1][0]:
            return True
        elif (cards[0][0] - 1) == cards[1][0]:
            return True
        
        # Check Ace-2 case.
        elif cards[0][0] == 14:
            if cards[1][0] == 2:
                return True
            else: return False
        
        elif cards[0][0] == 2:
            if cards[1][0] == 14:
                return True
            else:
                return False
            
        else:
            return False
        

    def get_suited_cards(self, suit, cards):
        """ Generate a suited hand type. """

        potential_cards = list(filter(lambda x: x[1] == suit, cards))
        return potential_cards
    

    def get_pair_cards(self, value, cards):
        """ Generate a pair hand type. """

        potential_cards = list(filter(lambda x: x[0] == value, cards))
        return potential_cards
    

    def get_connected_cards(self, value, cards):
        """ Generate a connected hand type. """

        potential_cards = list(filter(lambda x: x[0] == value or x[0] + 1 == value, cards))
        return potential_cards
    

    def generate_hand(self, hand_type):
        """ Generate a certain hand type. """

        # Shuffle a deck of cards.
        deck = list(itertools.product(range(2,15), ['Spade', 'Heart', 'Diamond', 'Club']))
        playing_deck = deck.copy()
        np.random.shuffle(playing_deck)

        # Make a random hand based on a selected hand type from the 
        # shuffled playing deck of cards.
        players_hand = []

        if hand_type == 'suited':
            suits = ['Spade', 'Heart', 'Diamond', 'Club']
            np.random.shuffle(suits)
            suit = suits[0]

            players_hand = self.get_suited_cards(suit, playing_deck)[:2]
        
        elif hand_type == 'pairs':
            values = list(range(2, 15))
            np.random.shuffle(values)
            value = values[0]
            
            players_hand = self.get_pair_cards(value, playing_deck)[:2]

        elif hand_type == 'conected':
            values = list(range(2, 15))
            np.random.shuffle(values)
            value = values[0]

            players_hand = self.get_connected_cards(value, playing_deck)[:2]

        elif hand_type == 'conected_suited':
            suits = ['Spade', 'Heart', 'Diamond', 'Club']
            np.random.shuflle(suits)
            suit = suits[0]

            values = list(range(2, 15))
            np.random.shuffle(values)
            value = values[0]

            connected_cards = self.get_connected_cards(value, playing_deck)
            first_card = connected_cards[0]

            # Only get cards that aren't our card for the potential second card.
            potential_second_cards = list(filter(lambda x: x != first_card[0], connected_cards))
            second_cards = potential_second_cards[0]

            players_hand = [first_card, second_cards]

        else:
            return 'Unknown hand type!'
        
        return players_hand
            



        
    

        
        

    

