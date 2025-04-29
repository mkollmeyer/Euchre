import Cards.py as Cards
import Player.py as player

class Table:
    def __init__(self, player1: player.player, player2: player.player, 
                 player3: player.player, player4: player.player):
        self.players = [player1, player2, player3, player4]
        self.team1 = player.team(player1, player3, 0) 
        self.team2 = player.team(player2, player4, 0)
        self.teams = [self.team1, self.team2]
        self.turn = 0
        self.trump = ""
        self.teamcall = player.team

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
        newdeck = Cards.deck()
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
            if isinstance(i, player.bot):
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
                if isinstance(o, player.bot):
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

    def play_round(self, trump: str, teamcall: player.team):
        self.round_trump = trump
        self.winning_card = [Cards.card, int]
        self.winning_team = player.team
        self.leadsuit = ""
        self.playing = (self.turn+1)%4
        self.winning_player = 0
        self.team1.roundscore = 0
        self.team2.roundscore = 0
        for r in range(4):
            if isinstance(self.players[self.playing], player.bot):
                self.winning_card = self.players[self.playing].lead(self.round_trump)
                self.leadsuit = self.winning_card[0].suit
                for j in self.teams:
                    if j.isonteam(self.players[self.playing]):
                        self.winning_team = j
            for t in range(3):
                self.playing = (self.playing+1)%4
                if isinstance(self.players[self.playing], player.bot):
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