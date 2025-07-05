from random import choice
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def ace_transform(cards):
    one_index = cards.index(11)
    cards.remove(11)
    cards.insert(one_index, 1)


while True:
    another_game = input(
        "Do you want to play a game of Blackjack? (y/n): ").strip().lower()
    if another_game == 'y':
        print("Starting a new game of Blackjack...")
        player_cards = [choice(cards), choice(cards)]
        player_sum = sum(player_cards)
        dealer_cards = [choice(cards),]

        if player_sum > 21 and 11 in player_cards:
            ace_transform(player_cards)
        print(
            f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        while sum(player_cards) < 21:
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: ").strip().lower()
            if another_card == 'y':
                player_cards.append(choice(cards))
                print(
                    f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            else:
                break
            if sum(player_cards) > 21:
                if 11 in player_cards:
                    ace_transform(player_cards)
                    print(
                        f"Your cards: {player_cards}, current score: {sum(player_cards)}")
                else:
                    print("You went over 21! You lose!")
                    break
        if sum(player_cards) <= 21:
            dealer_cards.append(choice(cards))
            print(
                f"Dealer's cards: {dealer_cards}, current score: {sum(dealer_cards)}")
            while sum(dealer_cards) < 17:
                dealer_cards.append(choice(cards))
                print(
                    f"Dealer's cards: {dealer_cards}, current score: {sum(dealer_cards)}")
                if sum(dealer_cards) > 21:
                    if 11 in dealer_cards:
                        ace_transform(dealer_cards)
                        print(
                            f"Dealer's cards: {dealer_cards}, current score: {sum(dealer_cards)}")
                        continue
                    else:
                        print("Dealer went over 21! You win!")
            if sum(dealer_cards) == sum(player_cards):
                print("It's a draw!")
            elif sum(dealer_cards) > sum(player_cards):
                print("Dealer wins!")
            elif sum(dealer_cards) < sum(player_cards):
                print("You win!")
    else:
        print("Thank you for playing! Goodbye!")
        break


# import sys
# from random import choice


# def show_cards(name, info):
#     print(f"{name.title()} have:")
#     for card in info['cards']:
#         print(card)
#     print(f"Sum is {sum(info['cards'])}")

# def give_one_more_card():
#     player['cards'].append(choice(cards))
#     show_cards('player', player)

# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# one_more_game = True

# while one_more_game:
#     dealer = {
#         'cards': [choice(cards), choice(cards)]
#     }

#     player = {
#         'cards': [choice(cards), choice(cards)]
#     }

#     game_not_over = True
#     while game_not_over:
#         show_cards('player', player)
#         one_more_card = True
#         while one_more_card:
#             sum_player = sum(player['cards'])
#             ask_card = input('Do you want one more card? ')
#             if ask_card == 'y':
#                 give_one_more_card()
#                 if 11 in player['cards']:
#                     value_ace = int(input("Enter ace value: "))
#                     if value_ace == 1:
#                         index_ace = player['cards'].index(11)
#                         player['cards'][index_ace] = 1
#                         sum_player += 1
#                         show_cards('player', player)
#                 sum_player = sum(player['cards'])
#                 if sum_player > 21:
#                     print(f"You lose with {player['cards']}")
#                     one_more_card = False
#                     game_not_over = False
#             else:
#                 one_more_card = False
#         if game_not_over == False:
#             break
#         print('-----------------------------------')
#         print('No more cards')
#         print('-----------------------------------')
#         show_cards('dealer', dealer)
#         sum_dealer = sum(dealer['cards'])
#         if sum_dealer < 17:
#             print('Dealer sum is less then 17.. One more card to dealer..')
#             dealer['cards'].append(choice(cards))
#             sum_dealer = sum(dealer['cards'])
#             show_cards('dealer', dealer)

#         if sum_dealer > 21:
#             print(f"Dealer lose with {dealer['cards']}")
#         elif sum_dealer == sum_player:
#             print('Draw..')
#         elif sum_dealer > sum_player:
#             print('Dealer wins')
#         elif sum_dealer < sum_player:
#             print('Player wins')
#         game_not_over = False

#     one_more = input("One more game? ")
#     if one_more == 'n':
#         print('Goodbye!')
#         sys.exit()
