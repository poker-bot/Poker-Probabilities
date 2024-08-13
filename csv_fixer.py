import csv

def normalize_card(card):
    rank, suit = card
    rank_map = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
    suit_map = {'Spade': 's', 'Heart': 'h', 'Diamond': 'd', 'Club': 'c'}
    
    rank = rank_map.get(rank, str(rank))
    suit = suit_map[suit]
    
    return f"{rank}{suit}"

def normalize_pocket_cards(card1, card2):
    normalized_card1 = normalize_card(card1)
    normalized_card2 = normalize_card(card2)
    
    # Sort cards based on rank first, then suit
    if int(card1[0]) != int(card2[0]):
        return '_'.join(sorted([normalized_card1, normalized_card2], key=lambda x: int(x[:-1]) if x[:-1].isdigit() else {'J':11, 'Q':12, 'K':13, 'A':14}[x[:-1]]))
    else:
        return '_'.join(sorted([normalized_card1, normalized_card2], key=lambda x: x[-1]))

def process_csv(input_file, output_file):
    processed_data = []

    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pocket_cards = eval(row['Pocket Cards'])
            normalized_pocket_cards = normalize_pocket_cards(pocket_cards[0], pocket_cards[1])
            
            processed_row = {
                'pocket_cards': normalized_pocket_cards,
                'pair': row['Pair'],
                'suited': row['Suited'],
                'connected': row['Connected']
            }
            
            for i in range(1, 9):
                processed_row[f'win_pct{i}'] = row[f'Win Pct{i}']
            
            processed_data.append(processed_row)

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['pocket_cards', 'pair', 'suited', 'connected'] + [f'win_pct{i}' for i in range(1, 9)]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in processed_data:
            writer.writerow(row)

    print(f"Processed data has been written to {output_file}")

# Run the script
input_file = 'data/pocket_hand_wins.csv'
output_file = 'data/fixed_pocket_hand_wins.csv'
process_csv(input_file, output_file)