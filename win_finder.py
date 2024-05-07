# gameplay.py
# Aidan Nachi
# 2024.06.05
# 
# This file defines a win finder class that finds the best poker
# hand in a five-card draw.
# modified from: https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python.html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict


class win_finder():
    """ Implement a win finder. """

    def __init__(self):
        """ Create win finder instance. """

        # Numpy Seed for generating random numbers
        np.random.seed(0)


    def check_straight_flush(self, hand):
        """ Check for a straight flush. """

        if check_flush(hand):
            hand = get_flush(hand)
            if check_straight(hand) and len(hand) >= 5:
                return True
            else:
                return False
        else:
            return False
        

    def check_four_of_a_kind(self, hand):
        """ Check for four of a kind. """

        # Extract card values from the hand
        values = [i[0] for i in hand]

        # Keep count of occurences of each of the values.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1
        
        # CHECK FOR 4 OF A KIND
        if 4 in sorted(value_counts.values()):
            return True
        return False
    

    def get_quads(self, hand):
        """ Return quads in hand. """

        # Extract card values from the hand.
        values = [i[0] for i in hand]

        # Keep count of occurences of each of the values.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1

        # Return the value of values that occur 4 times.
        return sorted([k for k, v in value_counts.items() if v == 4])
    

    def check_full_house(self, hand):
        """ Check if hand is a full house. """

        # Extract card values from the hand.
        values = [i[0] for i in hand]

        # Keep count of occurences of each of the values.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1

        sorted_value_counts = sorted(value_counts.values())

        # CHECK FOR A FULL HOUSE
        # Check for a 3 of a kind.
        if 3 in sorted_value_counts.count:

            # Check for a second three of a kind.
            if sorted_value_counts.count(3) > 1:
                return True
            
            # Check for a pair.
            elif 2 in sorted_value_counts:
                return True
        
        return False
    

    def get_full_house(self, hand):
        """ Get the values of a full house. """

        # Extract the card values from the hand.
        values = [i[0] for i in hand]

        # Keep count of occurences of each of the values.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1
        
        # Return values of each card.
        return sorted([k for k, v in value_counts.items() if v == 3 or v == 2], reverse = True)
    
    
    def check_flush(self, hand):
        """ Check if the hand is a flush. """

        # Extract the card suits from the hand.
        suits = [i[0] for i in hand]

        # Keep count of occurences of each of the suits.
        suit_counts = defaultdict(lambda:0)

        for suit in suits:
            suit_counts[suits] += 1

        # CHECK FOR A FLUSH
        # Check if a suit occurs 5 times or more.
        if sorted(suit_counts.values(), reverse = True)[0] >= 5:
            return True
        else:
            return False
        

    def get_flush(self, hand):
        """ Get the high card of a flush. """

        # Extract the card suits from the hand.
        suits = [i[1] for i in hand]

        # Keep count of occurences of each of the suits.
        suit_counts = defaultdict(lambda:0)

        for suit in suits:
            suit_counts[suits] += 1

        # Find the count of the most frequent suit.
        top_suit_count = sorted(suit_counts.values(), reverse=True)[0]

        # Find the suit with the highest count. 
        top_suit = sorted([k for k,v in suit_counts.items() if v==top_suit_count], reverse=True)[0]

        # Store cards in a hand that have the most frequent suit.
        flush_cards = []
        for card in hand:
            if card[1] == top_suit:
                flush_cards.append(card)

        return flush_cards
    

    def five_consecutive_cards(self, number_set):
        """ Determine if a hand has five consecutve cards. """

        # Make sure the set has numbers in it.
        if len(number_set) < 5:
            return False
        
        # Group consecutive numbers in a number set.
        for w, z in itertools.groupby(number_set, lambda x, y = itertools.count(): next(y) - x):
            grouped = list(z)

            if len(grouped) >= 5:
                return True
            
        return False
    

    def get_highest_consecutive_cards(self, number_set):
        """ Get the highest card in a straight. """

        # Group consecutive numbbers in a numbers set.
        for w, z in itertools.groupby(number_set, lambda x, y = itertools.count(): next(y) - x):
            grouped = list(z)

            if len(grouped) >= 5:

                # Get the highest consecutive card.
                return sorted(grouped, reverse = True)[0]
            
    
    def check_straight(self, hand):
        """ Check if the hand is a straight. """

        # Extract the card values from a card.
        values = [i[0] for i in hand]

        # Keep count of the occurence of each value.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1
            



        
    

        
    

    

