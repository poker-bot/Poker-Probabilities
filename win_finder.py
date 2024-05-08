# gameplay.py
# Aidan Nachi
# 2024.06.05
# 
# This file defines a win finder class that finds the best poker
# hand in a five-card draw.
# Reference: https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python.html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict


class Win_finder():
    """ Implement a win finder. """

    def __init__(self):
        """ Create win finder instance. """

        # Numpy Seed for generating random numbers
        np.random.seed(0)


    def check_straight_flush(self, hand):
        """ Check for a straight flush. """

        if self.check_flush(hand):
            hand = self.get_flush(hand)
            if self.heck_straight(hand) and len(hand) >= 5:
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

        set_of_values = set(values)

        # Check for straight. 
        if self.five_consecutive_cards(set_of_values):
            return True
        
        # Check low ace straight case.
        else:
            low_straight = set([14, 2, 3, 4, 5,])
            if low_straight.issubset(set_of_values):
                return True
            return False
        

    def get_straight_top_card(self, hand):
        """ Find the top card in a straight. """

        # Extract the card values from a card.
        values = [i[0] for i in hand]

        # Keep count of the occurence of each value.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1

        # Return the high card.
        set_of_values = set(values)
        if self.five_consecutive_cards(set_of_values):
            return self.get_highest_consecutive_cards(set_of_values)
        
        # Return the 5 if the hand is a low ace straight.
        else:
            return 5
        

    def check_three_of_a_kind(self, hand):
        """ Check if the hand is a three of a kind. """

        # Extract the card values from a card.
        values = [i[0] for i in hand]

        # Keep count of the occurence of each value.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1

        # Check for 3 of the same cards.
        if 3 in sorted(value_counts.values()):
            return True
        else:
            return False
        
    
    def get_trips(self, hand):
        """ Get card values for trips. """

        # Extract the card values from a card.
        values = [i[0] for i in hand]

        # Keep count of the occurence of each value.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1

        # Get the card values with the corresponding value_counts of 3.
        return sorted([k for k, v in value_counts.items() if v == 3], reverse = True)
    

    def check_two_pairs(self, hand):
        """ Check if the hand is a two pair. """

        # Extract the values from each card.
        values = [i[0] for i in hand]

        # Keep count of the occurence of each value.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1

        # Check for two pairs in the hand.
        if sorted(value_counts.values()).count(2) >= 2:
            return True
        else:
            return False
        
    
    def check_one_pair(self, hand):
        """ Check if the hand contains a pair. """

        # Extract the values from each card.
        values = [i[0] for i in hand]

        # Keep count of the occurence of each value.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1
        
        # Check for card values that appear twice.
        if 2 in value_counts.values():
            return True
        else:
            return False
    

    def get_pairs(self, hand):
        """ Get the pairs from a hand. """

        # Extract the values from each card. 
        values = [i[0] for i in hand]

        # Keep count of the occurence of each value.
        value_counts = defaultdict(lambda:0)

        for v in values:
            value_counts[v] += 1

        # Get the pairs from the hand.
        return sorted([k for k, v in value_counts.items() if v == 2], reverse = True)
    

    def check_hand(self, hand):
        """ Find the hand type and return the value it holds. """

        # Give hand it's value. (Straight flush best & No hand worst)
        if self.check_straight_flush(hand):
            return 9
        if self.check_four_of_a_kind(hand):
            return 8
        if self.check_full_house(hand):
            return 7
        if self.check_flush(hand):
            return 6
        if self.check_straight(hand):
            return 5
        if self.check_three_of_a_kind(hand):
            return 4
        if self.check_two_pairs(hand):
            return 3
        if self.check_one_pair(hand):
            return 2
        else:
            return 1
        
    
    def hand_type(self, hand):
        """ Find what type of hand the hand is. """
        
        if self.check_straight_flush(hand):
            return 'straight flush'
        if self.check_four_of_a_kind(hand):
            return 'four of a kind'
        if self.check_full_house(hand):
            return 'full house'
        if self.check_flush(hand):
            return 'flush'
        if self.check_straight(hand):
            return 'straight'
        if self.check_three_of_a_kind(hand):
            return 'three of a kind'
        if self.check_two_pairs(hand):
            return 'two pairs'
        if self.check_one_pair(hand):
            return 'pair'
        else:
            return 'high cards'

    
    def get_high_cards(self, hand):
        """ Get the high cards from a hand. """

        # Extract card values from a hand.
        values = [i[0] for i in hand]
        return sorted(values, reverse = True)
    
    def compare(self, card1, card2):
        """ Compare two cards and return the higher card. """

        if card1 > card2:
            return 1
        elif card1 < card2:
            return 2
        else:
            return 0


    def compare_cards(self, first_hand, second_hand, num=None):
        """ Compare the high card in two hands. """

        first_hand_high_card = self.get_high_cards(first_hand)[:num]
        second_hand_high_card = self.get_high_cards(second_hand)[:num]

        for i in range(len(first_hand_high_card)):
            comparison = self.compare(first_hand_high_card[i], second_hand_high_card[i])
            if comparison != 0:
                return comparison
    

    def break_tie(self, first_hand, second_hand):
        """ Break tie if two hands have the same card. """

        # Get the hand for each hand we are breaking a tie for.
        hand_score = self.check_hand(first_hand)

        # If hands are straight flushes, the straights are compared and the
        # higher straight wins.
        if hand_score == 9:
            first_straight = self.get_straight_top_card(first_hand)
            second_straight = self.get_straight_top_card(second_hand)

            if first_straight > second_straight:
                return 1
            else:
                return 2
            
        # If the hands are both four of a kinds, the higher quads win.
        if hand_score == 8:
            first_quads = self.get_quads(first_hand)
            second_quads = self.get_quads(second_hand)

            if first_quads > second_quads:
                return 1
            else:
                return 2
        
        # If the hands are both full houses, the higher trips win, if the
        # trips are equivalent the higher pair wins.
        if hand_score == 7:
            
            # Only get the two cards that occur in the list.
            first_full_house = self.get_full_house(first_hand)[:2]
            second_full_house = self.get_full_house(second_hand)[:2]

            for i in range(len(first_full_house)):
                if first_full_house > second_full_house:
                    return 1
                elif first_full_house < second_full_house:
                    return 2
        
        # If the hands are both flushes, the flush with the higher high card
        # wins.
        if hand_score == 6:
            first_flush = self.get_flush(first_hand)
            second_flush = self.get_flush(second_hand)

            return self.compare_cards(first_flush, second_flush)
        
        # If the hands are both straights, the higher straight wins.
        if hand_score == 5:
            first_straight = self.get_straight_top_card(first_hand)
            second_straight = self.get_straight_top_card(second_hand)

            if first_straight > second_straight:
                return 1
            elif first_straight < second_straight:
                return 2
            else:
                return 0
            
        # If both hands are trips, the higher trips winm but if the trips are the same
        # the hand with the high card wins.
        if hand_score == 4:
            first_trips = self.get_trips(first_hand)
            second_trips = self.get_trips(second_hand)

            if first_trips > second_trips:
                return 1
            elif first_trips < second_trips:
                return 2
            
            else:

                # Get the two cards in the hand that aren't the trips.
                first_hand = list(filter(lambda x: x[0] != first_trips, first_hand))
                second_hand = list(filter(lambda x: x[0] != second_trips, second_hand))

                return self.compare_cards(first_hand, second_hand, 2)
            
        # If both hands are two pairs, then the higher two pair wins. If both of the two
        # pairs are the same the final card in the hand determines the winner.
        if hand_score == 3:
            first_pairs = self.get_pairs(first_hand)
            second_pairs = self.get_pairs(second_hand)

            if first_pairs[0] > second_pairs[0]:
                return 1
            elif first_pairs[0] < second_pairs[0]:
                return 2
            elif first_pairs[1] > second_pairs[1]:
                return 1
            elif first_pairs[1] < second_pairs[1]:
                return 2
            else:

                # Get the card in the hand that isn't either of the pairs.
                first_hand = list(filter(lambda x: x[0] != first_pairs, first_hand))
                second_hand = list(filter(lambda x: x[0] != second_pairs, second_hand))

                return self.compare_cards(first_hand, second_hand, 1)
            
        # If both hands are pairs, then the higher pair wins. If both of the pairs are the same, 
        # the high card in the hand wins.
        if hand_score == 2:
            first_pair = self.get_pairs(first_hand)
            second_pair = self.get_pairs(second_hand)

            if first_pair > second_pair:
                return 1
            if first_pair < second_pair:
                return 2
            else:

                # Get the three cards that aren't apart of the pair.
                first_hand = list(filter(lambda x: x[0] != first_pair, first_hand))
                second_hand = list(filter(lambda x: x[0] != second_pair, second_hand))

                return self.compare_cards(first_hand, second_hand, 3)
            
        # If both hands don't have a distinct hand, the high card wins.
        if hand_score == 1:
            return self.compare_cards(first_hand, second_hand)
        
        # If no winners are determined by any pf the comparisons the hands tie.
        return 0 


    def game_result(self, players_hand, other_players_hands, board):
        """ Determine if player won, lost, or tied.
            
        Determine outcome of the players hand (win, loss, or tie), given
        a series of hands and the cards on the board.
        """

        # Find the best hand out of all the other players hands
        # Start by comparing the first hand of all of them to all the others.
        best_other_player_hand = board + other_players_hands[0]

        for hand in other_players_hands:
            hand = hand + board

            if self.check_hand(hand) > self.check_hand(best_other_player_hand):
                best_other_player_hand = hand
            
            # Find the better hand if they are both the same.
            elif self.check_hand(hand) == self.check_hand(best_other_player_hand):
                tie_breaker = self.break_tie(hand, best_other_player_hand)

                if tie_breaker == 1:
                    best_other_player_hand = hand

        # Compare player's hand with the best hand from the other players.
        players_hand = players_hand + board

        if self.check_hand(players_hand) > self.check_hand(best_other_player_hand):
            return 'Win'
        
        # Find the better hand if they are both the same.
        elif self.check_hand(players_hand) == self.check_hand(best_other_player_hand):
            final_tie_breaker = self.break_tie(players_hand, best_other_player_hand)

            if final_tie_breaker == 2:
                return 'Loss'
            elif final_tie_breaker == 1:
                return 'Win'
            else:
                return 'Tie'
            
        else:
            return 'Loss'
        

    def winning_result(self, players_hands, board):
        """ Determine the winning card combination. 
        
        Determine what was the winning card combination, given
        a series of hands and the cards on the board. """

        # Find the winnning players hand.
        best_player_hand = board + players_hands[0]

        for hand in players_hands:
            hand = hand + board
            
            if self.check_hand(hand) > self.check_hand(best_player_hand):
                best_player_hand = hand

            # Find the better hand if they are both the same.
            elif self.check_hand(hand) == self.check_hand(best_player_hand):
                tie_breaker = self.break_tie(hand, best_player_hand)

                if tie_breaker == 1:
                    best_player_hand = hand
            
        # Get the winning hand.
        return self.hand_type(best_player_hand)


                


    