import random

class card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"The {self.rank} of {self.suit}"

class player:
    def __init__(self, hand: list):
        self.hand = hand

    def __str__(self):
        return f"{self.hand(0)}, {self.hand(1)}, {self.hand(2)}, {self.hand(3)}, {self.hand(4)}"

class deck:
    def __init__(self, player: player, cards: int):
        self.player = player
        self.cards = cards
        self.deck = [card("9", "clubs"), card("10", "clubs"), card("Jack", "clubs"), 
                card("Queen", "clubs"), card("King", "clubs"), card("Ace", "clubs"),
                card("9", "spades"), card("10", "spades"), card("Jack", "spades"), 
                card("Queen", "spades"), card("King", "spades"), card("Ace", "spades"),
                card("9", "diamonds"), card("10", "diamonds"), card("Jack", "diamonds"), 
                card("Queen", "diamonds"), card("King", "diamonds"), 
                card("Ace", "diamonds"),card("9", "hearts"), card("10", "hearts"), 
                card("Jack", "hearts"), card("Queen", "hearts"), card("King", "hearts"), 
                card("Ace", "hearts")]

    def shuffle(self):
        return random.shuffle(self.deck)
    
class team:
    def __init__(self, player1: player, player2: player, score: int):
        self.player1 = player1
        self.player2 = player2
        self.score = score

    def __str__(self):
        return f"Player1 cards: {self.player1},\n Player2 cards: {self.player2},\n Score: {self.score}"

def main():
    firstdeck = deck
    firstdeck.shuffle()
    player1 = player(firstdeck[0, 1, 2, 10, 11])
    player2 = player(firstdeck[3, 4, 12, 13, 14])
    player3 = player(firstdeck[5, 6, 7, 15, 16])
    player4 = player(firstdeck[8, 9, 17, 18, 19])
    team1 = (player1, player3, 0)
    team2 = (player2, player4, 0)

    print(team1)
    print(team2)

if __name__ == "__main__":
    main()