cards = []
total_points = 0

def get_scratched_points(card):
    scratched_points = 0
    for scratched_number in card['scratched_numbers']:
        if scratched_number in card['winning_numbers']:
            if scratched_points == 0:
                scratched_points += 1
            else:
                scratched_points *= 2
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
        total_points += card['scratched_points']
        cards.append(card)
        print(card)

print(f'\nTotal points: {total_points}')