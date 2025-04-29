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

    def lead(self, trump: str) -> list:
        self.offsuit = {}
        self.returncard = card
        self.max = 0
        self.get_ranking(trump)
        for i in self.pref_cards:
            if i.suit != trump:
                self.offsuit[i] = self.pref_cards[i]
        if len(self.offsuit) != 0:
            print(len(self.offsuit))
            for r in self.offsuit:
                if self.offsuit[r] > self.max:
                    self.returncard = r
        else:
            for r in self.pref_cards:
                if self.pref_cards[r] > self.max:
                    self.returncard = r
                    self.max = self.pref_cards[r]
        self.value = self.pref_cards[self.returncard]
        self.pref_cards.pop(self.returncard)
        return [self.returncard, self.value]
        
    def follow(self, suit: str, teamwinning: bool, winningscore: int, trump: str) -> list:
        self.followsuit = {}
        self.minscore = 13
        self.playcard = card
        self.leastwin = 13
        self.canplay = False
        for i in self.pref_cards:
            if i.suit == suit:
                self.followsuit[i] = self.pref_cards[i]
        if len(self.followsuit) != 0:
            if teamwinning:
                for h in self.followsuit:
                    if self.followsuit[h] < self.minscore:
                        self.minscore = self.followsuit[h]
                        self.playcard = h
                print("Follow suit and teammate winning")
                print(str(self.playcard))
                self.value = self.pref_cards[self.playcard]
                self.pref_cards.pop(self.playcard)
                return [self.playcard, self.value]
            else:
                for g in self.followsuit:
                    if self.followsuit[g] > winningscore and self.followsuit[g] < self.leastwin:
                        self.leastwin = self.followsuit[g]
                        self.playcard = g
                        self.canplay = True
                if self.canplay:
                    print("Follow suit and teammate losing, I can win")
                    print(str(self.playcard))
                    self.value = self.pref_cards[self.playcard]
                    self.pref_cards.pop(self.playcard)
                    return [self.playcard, self.value]
                else:
                    print("Follow suit and teammate losing, I can't win")
                    self.new_min = 12
                    for a in self.followsuit:
                        if self.pref_cards[a] < self.new_min:
                            self.playcard = a
                            self.new_min = self.pref_cards[a]
                    print(str(self.playcard))
                    self.value = self.pref_cards[self.playcard]
                    self.pref_cards.pop(self.playcard)
                    return [self.playcard, self.value]
        else:
            self.hastrump = False
            for l in self.pref_cards:
                if l.suit == trump and self.pref_cards[l] < self.minscore:
                    self.hastrump = True
                    self.playcard = l
                    self.minscore = self.pref_cards[l]
            if self.hastrump:
                print("I have trump so I can win")
                print(str(self.playcard))
                self.value = self.pref_cards[self.playcard]
                self.pref_cards.pop(self.playcard)
                return [self.playcard, self.value]
            else:
                for q in self.pref_cards:
                    if self.pref_cards[q] < self.minscore:
                        self.playcard = q
                print("I dont have trump so I can't win")
                print(str(self.playcard))
                self.value = self.pref_cards[self.playcard]
                self.pref_cards.pop(self.playcard)
                return [self.playcard, 0]

    def print_rank(self):
        card_rank = ""
        for i in self.pref_cards:
            card_rank += (str(i) + " " + str(self.pref_cards[i]) + "\n")
        print(card_rank)
        return 0
    
    def pickup_or_pass(self, isteam: bool, trump: str, dealer: player = None, rank = "0") -> bool:
        total = 0
        hasbauer = False
        for i in self.pref_cards:
            total += self.pref_cards[i]
            if (self.pref_cards[i] > 10):
                hasbauer = True
        if isteam:
            total += self.trump_rank[rank]
        else:
            total -= self.trump_rank[rank]
        if total > 30 and hasbauer:
            if rank != "0":
                self.min = 13
                self.discard = card
                for w in dealer.pref_cards:
                    if dealer.pref_cards[w] < self.min:
                        self.min = dealer.pref_cards[w]
                        self.discard = w
                dealer.hand.remove(self.discard)
                dealer.hand.append(card(rank, trump))
                dealer.get_ranking(trump)
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
        self.roundscore = int

    def isonteam(self, player: player) -> bool:
        if player == self.player1 or player == self.player2:
            return True
        else:
            return False
    
    def loner(self) -> bool:
        return False

    def __str__(self):
        teamcards = "Player1 cards: " + str(self.player1) +"Player2 cards: "
        teamcards += str(self.player2) + "Score: "
        teamcards += str(self.score) + "\n"
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
        
    def end_game(self) -> bool:
        for u in self.teams:
            if u.score > 9:
                return True

    def set_round(self):
        self.suits = ["diamonds", "hearts", "clubs", "spades"]
        newdeck = deck()
        newdeck.shuffle()
        self.call = False
        self.callsuit = False
        self.play = True
        self.deals = 0
        self.dealer = (self.deals)%4
        self.players[(self.turn)%4].get_hand(newdeck.card()[0:3] + newdeck.card()[10:12])
        self.players[(self.turn+1)%4].get_hand(newdeck.card()[3:5] + newdeck.card()[12:15])
        self.players[(self.turn+2)%4].get_hand(newdeck.card()[5:8] + newdeck.card()[15:17])
        self.players[(self.turn+3)%4].get_hand(newdeck.card()[8:10] + newdeck.card()[17:20])
        self.turnup = newdeck.card()[20]
        for i in self.players:
            if isinstance(i, bot):
                i.get_ranking(self.turnup.suit)
                if i.pickup_or_pass(self.isteammate(self.players.index(i)), 
                                    self.turnup.suit, self.players[self.dealer], self.turnup.rank):
                    self.trump = self.turnup.suit
                    for m in self.teams:
                        if m.isonteam(i):
                            self.teamcall = m
                            self.call = True
                            self.callsuit = True
                            print(str(self.turnup))
                        #print(str(m))
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
                                    self.callsuit = True
                                    print(str(self.trump))
                                #print(str(m))
        if not(self.callsuit):
            self.turn += 1
            print("pass")
            self.play = False
        self.deals += 1

    def play_round(self, trump: str, teamcall: team):
        self.round_trump = trump
        self.winning_card = [card, int]
        self.winning_team = team
        self.leadsuit = ""
        self.playing = (self.turn+1)%4
        self.winning_player = 0
        self.team1.roundscore = 0
        self.team2.roundscore = 0
        for r in range(4):
            if isinstance(self.players[self.playing], bot):
                self.winning_card = self.players[self.playing].lead(self.round_trump)
                self.leadsuit = self.winning_card[0].suit
                for j in self.teams:
                    if j.isonteam(self.players[self.playing]):
                        self.winning_team = j
            for t in range(3):
                self.playing = (self.playing+1)%4
                if isinstance(self.players[self.playing], bot):
                    self.played = self.players[self.playing].follow(self.leadsuit, self.winning_team.isonteam(self.players[self.playing]),
                                                                       self.winning_card[1], self.round_trump)
                    if self.winning_card[1] < self.played[1]:
                        self.winning_card = self.played
                        for f in self.teams:
                            if f.isonteam(self.players[self.playing]):
                                self.winning_team = f
                                self.winning_player = self.playing
                print(str(len(self.players[self.playing].pref_cards)) + " cards left")
            self.winning_team.roundscore += 1
            self.playing = self.winning_player

        for b in self.teams:
            if b.roundscore == 5:
                b.score += 2
            elif (b.roundscore == 3 or b.roundscore == 4) and b == teamcall:
                b.score += 1
            elif (b.roundscore == 3 or b.roundscore == 4) and b != teamcall:
                b.score += 2
        



def main():
    p1 = bot()
    p2 = bot()
    p3 = bot()
    p4 = bot()
    playtable = Table(p1, p2, p3, p4)
    while not playtable.end_game():
        playtable.set_round()
        if playtable.play:
            playtable.play_round(playtable.trump, playtable.teamcall)


if __name__ == "__main__":
    main()