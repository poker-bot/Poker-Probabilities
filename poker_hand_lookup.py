import csv

# Card rankings and suit mappings
rank_map = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
suit_map = {'Spade': 's', 'Heart': 'h', 'Diamond': 'd', 'Club': 'c'}
reverse_rank_map = {v: k for k, v in rank_map.items()}

# Read the CSV file
with open('data/fixed_pocket_hand_wins.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    hand_data = {row['pocket_cards']: row for row in csv_reader}

def normalize_cards(card1, card2):
    """Normalize the order of two cards."""
    rank1, suit1 = card1[0], card1[1]
    rank2, suit2 = card2[0], card2[1]
    
    # Convert ranks to numerical values
    rank1_val = reverse_rank_map[rank1]
    rank2_val = reverse_rank_map[rank2]
    
    # Always put the higher rank (or Ace) second
    if rank1_val > rank2_val or rank1 == 'A':
        return f"{card2}_{card1}"
    elif rank1_val < rank2_val or rank2 == 'A':
        return f"{card1}_{card2}"
    else:  # Same rank, order by suit
        if suit1 > suit2:
            return f"{card2}_{card1}"
        else:
            return f"{card1}_{card2}"

def get_hand_data(card1, card2):
    """Get the row data for a given card pairing."""
    normalized_hand = normalize_cards(card1, card2)
    result = hand_data.get(normalized_hand, "Hand not found in the dataset.")
    # print(f"Debug: Lookup for {normalized_hand} resulted in: {result}")
    return result

# Example usage
hand_data = get_hand_data("Kh", "Ts")

print(f"Pocket cards: {hand_data['pocket_cards']}")
print(f"Pair: {hand_data['pair']}")
print(f"Suited: {hand_data['suited']}")
print(f"Connected: {hand_data['connected']}")
for i in range(1, 9):
    print(f"Win percentage {i} player: {hand_data[f'win_pct{i}']}%")

