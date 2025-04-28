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
        self.ranking = {"Ace":5, "King":4, "Queen":3, "Jack":2, "10":1, "9":0}
        self.trump_rank = {"Jack":12, "Left":11, "Ace":10, "King":9, "Queen":8, "10":7, "9":6}
        self.pref_cards = dict

    def get_ranking(self, trump: str):
        self.pref_cards = {}
        for i in self.hand:
            if i.suit == trump:
                for o in self.trump_rank:
                    if i.rank == o:
                        self.pref_cards[i] = self.trump_rank[o]
            elif trump == "diamonds" and i.suit == "hearts" and i.rank == "Jack":
                self.pref_cards[i] = 11
            elif trump == "heats" and i.suit == "diamonds" and i.rank == "Jack":
                self.pref_cards[i] = 11
            elif trump == "spades" and i.suit == "clubs" and i.rank == "Jack":
                self.pref_cards[i] = 11
            elif trump == "clubs" and i.suit == "spades" and i.rank == "Jack":
                self.pref_cards[i] = 11
            else:
                for o in self.ranking:
                    if i.rank == o:
                        self.pref_cards[i] = self.ranking[o]

    def print_rank(self):
        card_rank = ""
        for i in self.pref_cards:
            card_rank += (str(i) + " " + str(self.pref_cards[i]) + "\n")
        print(card_rank)
        return 0

    def __str__(self):
        current = ""
        for i in self.hand:
            current += str(i)
            current += " "
        return f"{current}\n"
    
class bot(player):
    def __init__(self, hand):
        player.__init__(self, hand)
            
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
    
class team:
    def __init__(self, player1: player, player2: player, score: int):
        self.player1 = player1
        self.player2 = player2
        self.score = score

    def __str__(self):
        teamcards = "Player1 cards: " + str(self.player1) +"\nPlayer2 cards: "
        teamcards += str(self.player2) + "\nScore: "
        teamcards += str(self.score)
        return teamcards

def main():
    firstdeck = deck()
    firstdeck.shuffle()
    player1 = player(firstdeck.card()[0:3] + firstdeck.card()[10:12])
    player2 = player(firstdeck.card()[3:5] + firstdeck.card()[12:15])
    player3 = player(firstdeck.card()[5:8] + firstdeck.card()[15:17])
    player4 = player(firstdeck.card()[8:10]+firstdeck.card()[17:20])
    team1 = team(player1, player3, 0)
    team2 = team(player2, player4, 0)

    player1.get_ranking("clubs")
    player1.print_rank()

if __name__ == "__main__":
    main()