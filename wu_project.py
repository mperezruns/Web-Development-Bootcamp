import random
# SINGLE CARD CLASS
# CREATING A CARD CLASS WITH OUTSIDE VARIABLES
# SUIT, RANK, VALUES
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
            'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# DEFINING A CLASS FOR THE CARDS
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

three_of_clubs = Card("Clubs", 'Three')

# Create an example card
print(suits[0])
print(ranks[0])
two_hearts = Card(suits[0], ranks[0])
print(two_hearts)


# DECK CLASS
# USING A CLASS WITHIN ANOTHER CLASS
class Deck:

    def __init__(self):
        # This only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        # This doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # This remove one card from the list of all_cards
        return self.all_cards.pop()

# CREATING THE 52 DECK OF CARDS
mydeck = Deck()
print(len(mydeck.all_cards))

mydeck.all_cards[0]
# print(mydeck.all_cards[0])

# Shuffle the deck
mydeck.shuffle()
print(mydeck.all_cards[0])

my_card = mydeck.deal_one()
print(my_card)

# PLAYER CLASS
class Player:

    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        # Note we remove one card from the List of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)  # pop() method removes the item at the given index from the list and returns the removed item.

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)


    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# DEFINING MARK AS A PLAYER
mark = Player("Mark")
mark

# THE OUTPUT RETURNS THE NUMBER OF CARDS GIVEN TO THE PLAYER
print(mark)
# MARK HAS A CARD
two_hearts
mark.add_cards(two_hearts)
print(mark)

# MARK NOW HAS A TOTAL FOR FOUR CARDS
mark.add_cards([two_hearts,two_hearts,two_hearts])
print(mark)

# WAR GAME LOGIC
player_one = Player("One")
player_two = Player("Two")

# SETUP NEW GAME
new_deck = Deck()
new_deck.shuffle()

# SPLIT THE DECK BETWEEN PLAYERS
print(len(new_deck.all_cards) / 2)

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(len(new_deck.all_cards))
print(len(player_one.all_cards))
print(len(player_two.all_cards))