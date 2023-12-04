cards = []
total_points = 0

def get_scratched_points(card):
    scratched_points = 0
    for scratched_number in card['scratched_numbers']:
        if scratched_number in card['winning_numbers']:
            scratched_points += 1
    return scratched_points


with open('2023/4/input.txt', 'r') as file:
    for line in file:
        card_number, numbers = line.split(':')
        winning_numbers, scratched_numbers = numbers.split('|')
        card = {
            'card_number': int(card_number.strip().split()[1]),
            'winning_numbers': list(map(int, winning_numbers.strip().split())),
            'scratched_numbers': list(map(int, scratched_numbers.strip().split()))
        }
        card['scratched_points'] = get_scratched_points(card)
        cards.append(card)


def recurse(cardid, totalcards):
    print(f'Card {cardid} has {cards[cardid-1]["scratched_points"]} points')
    for i in range(cardid, cardid+cards[cardid-1]['scratched_points']):
        if i < len(cards):
            totalcards += 1
            totalcards = recurse(i+1, totalcards)
    return totalcards

totalcards = 0
for card in cards:
    print(f'INIT Card {card["card_number"]}')
    totalcards += 1
    totalcards = recurse(card['card_number'], totalcards)
print(totalcards)