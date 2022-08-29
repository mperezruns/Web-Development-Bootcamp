import pdb
# PLAY THE SIMPLE WAR GAME
from wu_project import Card
from wu_project import Deck
from wu_project import Player

# GAME SETUP
game_on = True

# PLAYERS
player_one = Player("One")
player_two = Player("Two")

round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        game_on = False
        break

    # Otherwise, the game continues!

    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one_cards.remove())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one_cards.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        # Player Two Has Higher Cards
        elif player_one_cards[-1].value < player_one_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # This will grab another card and contine the current war.

            # First check to see if player has enough cards.
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.add_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player Two Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

# GAME SETUP
# PLAYERS
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break

    # Otherwise, the game continues!

    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            # No longer at "war" , time for the next round
            at_war = False

        # Player Two Has Higher Card
        elif player_two_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False
        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War!")
                print("Player One Wins! Player Two Loses!")
                game_on = False
                break
            # Otherwise, the war continues and more cards are added
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())