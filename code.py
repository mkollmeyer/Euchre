import random

class card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"The {self.rank} of {self.suit}"

class player:
    def __init__(self):
        self.hand = list

    def get_hand(self, hand: list):
        self.hand = hand

    def __str__(self):
        current = ""
        for i in self.hand:
            current += str(i)
            current += " "
        return f"{current}\n"
    
class bot(player):
    def __init__(self):
        super().__init__()
        self.ranking = {"Ace":5, "King":4, "Queen":3, "Jack":2, "10":1, "9":0}
        self.trump_rank = {"Jack":12, "Left":11, "Ace":10, "King":9, "Queen":8, "10":7, "9":6, "0":0}
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
    
    def pickup_or_pass(self, isteam: bool, trump: str, rank = "0") -> bool:
        total = 0
        hasbauer = False
        for i in self.hand:
            total += self.pref_cards[i]
            if (i.rank == "Jack" and i.suit == trump) or rank == "Jack":
                hasbauer = True
        if isteam:
            total += self.trump_rank[rank]
        else:
            total -= self.trump_rank[rank]
        if total > 30 and hasbauer:
            return True
        else:
            return False

            
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

    def isonteam(self, player: player) -> bool:
        if player == self.player1 or player == self.player2:
            return True
        else:
            return False

    def __str__(self):
        teamcards = "Player1 cards: " + str(self.player1) +"\nPlayer2 cards: "
        teamcards += str(self.player2) + "\nScore: "
        teamcards += str(self.score)
        return teamcards
    
class Table:
    def __init__(self, player1: player, player2: player, player3: player, player4: player):
        self.players = [player1, player2, player3, player4]
        self.team1 = team(player1, player3, 0) 
        self.team2 = team(player2, player4, 0)
        self.teams = [self.team1, self.team2]
        self.turn = 0
        self.trump = ""
        self.teamcall = team

    def isteammate(self, play: int) -> bool:
        if ((self.turn)%4+play)%2 == 0:
            return True
        else:
            return False

    def set_round(self):
        self.suits = ["diamonds", "hearts", "clubs", "spades"]
        newdeck = deck()
        newdeck.shuffle()
        self.call = False
        self.players[(self.turn)%4].get_hand(newdeck.card()[0:3] + newdeck.card()[10:12])
        self.players[(self.turn+1)%4].get_hand(newdeck.card()[3:5] + newdeck.card()[12:15])
        self.players[(self.turn+2)%4].get_hand(newdeck.card()[5:8] + newdeck.card()[15:17])
        self.players[(self.turn+3)%4].get_hand(newdeck.card()[8:10] + newdeck.card()[17:20])
        self.turnup = newdeck.card()[20]
        for i in self.players:
            if isinstance(i, bot):
                i.get_ranking(self.turnup.suit)
                if i.pickup_or_pass(self.isteammate(self.players.index(i)), 
                                    self.turnup.suit, self.turnup.rank):
                    self.trump = self.turnup.suit
                    for m in self.teams:
                        if m.isonteam(i):
                            self.teamcall = m
                            self.call = True
                            print(str(self.turnup))
                            print(str(m))
        if not (self.call):
            self.suits.remove(self.turnup.suit)
            for o in self.players:
                if isinstance(o, bot):
                    for p in self.suits:
                        o.get_ranking(p)
                        if i.pickup_or_pass(self.isteammate(self.players.index(i)), p):
                            self.trump = p
                            for m in self.teams:
                                if m.isonteam(o):
                                    self.teamcall = m
                                    self.call = True
                                    print(str(self.trump))
                                    print(str(m))
        if not(self.call):
            self.turn += 1
            print("pass")

def main():
    p1 = bot()
    p2 = bot()
    p3 = bot()
    p4 = bot()
    playtable = Table(p1, p2, p3, p4)
    playtable.set_round()


if __name__ == "__main__":
    main()