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
