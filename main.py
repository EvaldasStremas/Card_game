import random
import os
import sys


def create_card_deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    card_number = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    all_cards = []

    for x in range(len(suits)):
        for y in range(len(card_number)):
            card = suits[x], card_number[y]
            all_cards.append(card)

    return all_cards


def get_player_card(all_cards, player):
    if len(all_cards) <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("No left cards! Please try again")
        input('Press ENTER to continue')
        sys.exit()

    new_card = random.choice(range(len(all_cards)))
    main_card = all_cards[new_card]
    print(player, 'player new card is:', main_card[0] + ' ' + main_card[1])
    all_cards.remove(all_cards[new_card])
    print('Left cards in deck:', len(all_cards))
    print()

    return main_card


def check_game_winner(player_main_card, new_card, player):
    if player_main_card[1] == new_card[1]:
        print('***', player, 'player is winner ***')
        print()
        input('Press ENTER to continue')
        sys.exit()

    return None


# ------------------------------------MAIN-----------------------------------------

def main():
    game_over = False
    game_iteration = 0

    all_cards = create_card_deck()
    random.shuffle(all_cards)
    input('Cards shuffled. Press ENTER to continue')
    os.system('cls' if os.name == 'nt' else 'clear')

    first_player_main_card = get_player_card(all_cards, 'First')
    second_player_main_card = get_player_card(all_cards, 'Second')
    input()

    while not game_over:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('First player main card is:', first_player_main_card[0] + ' ' + first_player_main_card[1])
        new_card = get_player_card(all_cards, 'First')
        check_game_winner(first_player_main_card, new_card, 'First')

        print('Second player main card is:', second_player_main_card[0] + ' ' + second_player_main_card[1])
        new_card = get_player_card(all_cards, 'Second')
        check_game_winner(second_player_main_card, new_card, 'Second')

        game_iteration = game_iteration + 1
        print('Game iteration:', game_iteration)
        input('Press ENTER to continue')


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()