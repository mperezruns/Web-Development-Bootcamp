# Milestone Project 2 - Blackjack

# The Blackjack Game

# Imports and Global Variables
import random
# Step 1: Import the random module. This will be used to shuffle the deck prior to dealing.
# Then, declare variables to store suits, ranks and values. You can develop your own system, or copy ours below.
# Finally, declare a Boolean value to be used to control while loops. This is a common practice used to control the flow of the game.

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

# Step 2: Create a Card Class
# A card object needs two attributes: suit and rank. Add an attribute for "value"
# In addition to the Card's __init__ method, consider adding a __str__ method that, when asked to print a Card, returns a string in the form "Two of Hearts"
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit

# Step 3: Create a Deck Class
# Here the 52 card objects is stored in a list that can later be shuffled.
# First, though, we need to instantiate all 52 unique card objects and add them to the list.
# So long as the Card class definition appears in our code, we can build Card objects inside our Deck __init__ method
class Deck:

    def __init__(self):
        self.deck = [] # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The Deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# TESTING: TO SEE WHAT THE DECK OF CARDS LOOKS LIKE!
test_deck = Deck()
test_deck.shuffle()
print(test_deck)

# Step 4: Create a Hand Class
# In addition to holding Card objects dealt from the Deck,
# the Hand class may be used to calculate the value of those cards using the values dictionary defined above.
# It may also need to adjust for the value of Aces when appropriate.
class Hand:
    def __init__(self):
        self.cards = [] # start with an empty list like in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0   # add an attribute to keep track of aces

    def add_card(self,card):
        # card passed in
        # from Deck.deal() --> single Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        # THAN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
        while self.value > 21 and self.aces > 0:
            self.values -= 10
            self.aces -= 1

zero = 0
one = 1
two = 2

if 1:
    print('TRUE')

test_deck = Deck()
test_deck.shuffle()

# PLAYER
test_player = Hand()
# Deal 1 card from the deck CARD(suit, rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

test_player.add_card(test_deck.deal())
test_player.value

# Step 5: Create a Chip class
# In addition to decks of cards and hands, we need to keep track of a Player's starting chips, bets, and ongoing winnings.
# This could be done using global variables, but in the spirit of object oriented programming, let's make a Chips class instead!
class Chips:

    def __init__(self):
        self.total = 100    # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# Step 6: Write a function for taking bets
# Since we're asking the user for an integer value, this would be a good place to use try/except.
# Remember to check that a Player's bet can be covered by their available chips.
def take_bet():

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have: {}'.format(chips.total))
            else:
                break

# Step 7: Write a function for taking hits
# Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17.
# It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand.
# You may want it to check for aces in the event that a player's hand exceeds 21.
def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

# Step 8: Write a function prompting the Player to Hit or Stand
# This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.
# If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False - this will control the behavior of a while loop later on in our code.
def hit_or_stand(deck, hand):
    global playing # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s ')    # HIT # hh # stand

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print("Sorry, I did not understand that, Please enter h or s only!!")
            continue
        break

# Step 9: Write functions to display cards
# When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's cards are visible.
# At the end of the hand all cards are shown, and you may want to show each hand's total value. Write a function for each of these scenarios.
def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    # show all the dealer's cards
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


