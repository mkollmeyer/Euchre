import random

class card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"The {self.rank} of {self.suit}"

class deck:
    def __init__(self):
        self.cards = [card("9", "clubs"), card("10", "clubs"), card("Jack", "clubs"), 
                card("Queen", "clubs"), card("King", "clubs"), card("Ace", "clubs"),
                card("9", "spades"), card("10", "spades"), card("Jack", "spades"), 
                card("Queen", "spades"), card("King", "spades"), card("Ace", "spades"),
                card("9", "diamonds"), card("10", "diamonds"), card("Jack", "diamonds"), 
                card("Queen", "diamonds"), card("King", "diamonds"), 
                card("Ace", "diamonds"),card("9", "hearts"), card("10", "hearts"), 
                card("Jack", "hearts"), card("Queen", "hearts"), card("King", "hearts"), 
                card("Ace", "hearts")]
        
    def shuffle(self):
        return random.shuffle(self.cards)
        
    def card(self):
        return self.cards