import random
import os

def player_main_card(all_cards, player, game_iteration):
    new_card = random.choice(range(len(all_cards)))

    
    # print(player,'player main card is:', first_player_main_card)
    # first_player_main_card = all_cards[new_card]

    # if game_iteration != 0:
    #     print(player,'player new card is:', all_cards[new_card])

    print(player,'player new card is:', all_cards[new_card])

    # Remove first player card from deck
    all_cards.remove(all_cards[new_card])
    print('Left cards in deck:', len(all_cards))

    return None

# ------------------------------------MAIN-----------------------------------------

def main():
    game_over = False
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    card_number = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    all_cards = []
    game_iteration = 0

    for x in range(len(suits)):
        for y in range(len(card_number)):
            card = suits[x] + ' ' + card_number[y]
            all_cards.append(card)

    random.shuffle(all_cards)
    input('Cards are shuffled. Press ENTER to continue')

    while not game_over:
        os.system('cls' if os.name == 'nt' else 'clear')

        
        player_main_card(all_cards, 'First', game_iteration)
        print()
        player_main_card(all_cards, 'Second', game_iteration)
        print()

        game_iteration = game_iteration + 1
        print('Game iteration:', game_iteration)

        input('Press ENTER to continue')

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()