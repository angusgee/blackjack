import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card() -> int:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card:int = cards[random.randint(0, 12)]
    return new_card

def calculate_score(arr:list[int]) -> int:
    return sum(arr)

def check_blackjack(score: int, cards:list[int]) -> bool:
    if score == 21 and 11 in cards:
        return True 
    else:
        return False

def check_busted(score:int) -> bool:
    if score > 21:
        return True
    else:
        return False

def lose():
    print('player loses - better luck next time 😭')

def win():
    print('You win!! 🎉🎉')

def main():

    # Start game
    print(logo)

    # Calculate starting cards
    player_cards:list[int] = []
    computer_cards:list[int] = []

    player_cards.append(deal_card())
    player_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)


    print(f'Player has: {player_cards}')
    print(f'Computer has: {computer_cards}')
    print(f'Player\'s score: {player_score}')
    print(f'Computer\'s score: {computer_score}')

    # Check for Blackjack
    if check_blackjack(computer_cards, computer_score):
        lose()
    elif check_blackjack(player_cards, player_score):
        win()
    else:
        pass

    if check_busted(player_score):
        lose()


if __name__ == '__main__':
    main()

# take_card = input((f'Take another card? y/n: ')).lower()

# if take_card == 'y':
#     player_cards.append(deal_card())
#     print(f'Player has: {player_cards}')
#     print(f'Player\'s score: {player_score}')

    


