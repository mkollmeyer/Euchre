import Cards.py as Cards

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
        self.returncard = Cards.card
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
        self.playcard = Cards.card
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
                self.discard = Cards.card
                for w in dealer.pref_cards:
                    if dealer.pref_cards[w] < self.min:
                        self.min = dealer.pref_cards[w]
                        self.discard = w
                dealer.hand.remove(self.discard)
                dealer.hand.append(Cards.card(rank, trump))
                dealer.get_ranking(trump)
            return True
        else:
            return False