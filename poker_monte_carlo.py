import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict


class Poker_monte_carlo():
    """ Implement a Monte Carlo Simulation for a game of poker. """

    def __init__(self):
        """ Create win finder instance. """

        # Numpy Seed for generating random numbers
        np.random.seed(0)
        self.deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))
        self.second_deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))

    def check_straight_flush(self, hand):
        """ Check for a straight flush. """

        if self.check_flush(hand):
            hand = self.get_flush(hand)
            if self.check_straight(hand) and len(hand) >= 5:
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
        return sorted([k for k, v in value_counts.items() if v == 4], reverse=True)
    

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
        if 3 in sorted_value_counts:

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

        sorted_value_counts = sorted(value_counts.values())
 
        # Return values of each card.
        return sorted([k for k, v in value_counts.items() if v == 3 or v == 2], reverse = True)
    
    
    def check_flush(self, hand):
        """ Check if the hand is a flush. """

        # Extract the card suits from the hand.
        suits = [i[1] for i in hand]

        # Keep count of occurences of each of the suits.
        suit_counts = defaultdict(lambda:0)

        for suit in suits:
            suit_counts[suit] += 1

        # CHECK FOR A FLUSH
        # Check if a suit occurs 5 times or more.
        if sorted(suit_counts.values(), reverse=True)[0] >= 5:
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
            suit_counts[suit] += 1

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
        for w, z in itertools.groupby(number_set, lambda x, y=itertools.count(): next(y)-x):
            grouped = list(z)

            if len(grouped) >= 5:
                return True
            
        return False
    

    def get_highest_consecutive_card(self, number_set):
        """ Get the highest card in a straight. """

        # Group consecutive numbbers in a numbers set.
        for w, z in itertools.groupby(number_set, lambda x, y=itertools.count(): next(y)-x):
            grouped = list(z)

            if len(grouped) >= 5:

                # Get the highest consecutive card.
                return sorted(grouped, reverse=True)[0]
            
    
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
            return self.get_highest_consecutive_card(set_of_values)
        
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
        return sorted([k for k, v in value_counts.items() if v==3], reverse=True)
    

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
        return sorted([k for k, v in value_counts.items() if v == 2], reverse=True)
    

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

        first_hand_high_cards = self.get_high_cards(first_hand)[:num]
        second_hand_high_cards = self.get_high_cards(second_hand)[:num]

        for i in range(len(first_hand_high_cards)):
            comparison = self.compare(first_hand_high_cards[i], second_hand_high_cards[i])
            if comparison != 0:
                return comparison
            
        return 0


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
            first_quads = self.get_quads(first_hand)[0]
            second_quads = self.get_quads(second_hand)[0]

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
                if first_full_house[i] > second_full_house[i]:
                    return 1
                elif first_full_house[i] < second_full_house[i]:
                    return 2
        
        # If the hands are both flushes, the flush with the higher high card
        # wins.
        if hand_score == 6:
            first_flush = self.get_flush(first_hand)
            second_flush = self.get_flush(second_hand)

            return self.compare_cards(first_flush, second_flush, 5)
        
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
            first_trips = self.get_trips(first_hand)[0]
            second_trips = self.get_trips(second_hand)[0]

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
            return tie
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

        # Draw four cards from the deck and burn the top card.
        flop = playing_deck[0:4]
        del playing_deck[0:4]
        del flop[0]

        # Turn and burn the first two cards in the deck.
        turn = playing_deck[0:2]
        del playing_deck[0:2]
        del turn[0]

        # Draw two cards burn one and flip the final river card.
        river = playing_deck[0:2]
        del playing_deck[0:2]
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
        return self.game_result(players_hand, other_players_hands, board)
    

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
        return self.winning_result(players_hands, board)
    

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
            np.random.shuffle(suits)
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
    
    def pocket_hand_analysis(self):
        """ Collect data for pocket hand winning percentages. 

        Go through every possible pocket cards combo and record the winning %
        for games with varrying amounts of other players.
        """


        # Set up the simulation with the deck, hand combos, and the amount of games
        # simulated.
        pocket_deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))
        hand_combinations = list(itertools.combinations(pocket_deck, 2))
        hand_combinations = [list(row) for row in hand_combinations]
        num_of_folding_players = 0
        game_simulations = 1000

        # Choose random hands when simulating.
        np.random.shuffle(hand_combinations)

        columns = ['Pocket Cards', 'Pair', 'Suited', 'Connected', 'Win Pct1', 'Win Pct2', 'Win Pct3', 'Win Pct4', 'Win Pct5', 'Win Pct6', 'Win Pct7', 'Win Pct8']
        hands_df = pd.DataFrame(columns=columns)


        # Simulate desired amount of poker games.
        for hand in hand_combinations:
                pocket_cards = str(hand)
                each_hands_data_dict = {'Pocket Cards': pocket_cards, 
                                        'Pair': self.is_pocket_pair(hand), 
                                        'Suited': self.is_suited(hand), 
                                        'Connected': self.is_connected(hand),
                                        }
                for i in range(1, 9):
                    each_hands_data_dict['Win Pct' + str(i)] = self.play_game(hand, i, game_simulations, num_of_folding_players)

                new_row_df = pd.DataFrame(each_hands_data_dict, index=[0])
                hands_df = pd.concat([hands_df, new_row_df], ignore_index=True)
                    


        # Store data frame of simulated games in a csv.
        print(hands_df)
        hands_df.to_csv('data/pocket_hand_wins.csv')



            



        
    

        
        

    






        




                


    