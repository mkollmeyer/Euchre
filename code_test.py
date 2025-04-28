import unittest
import code

class tests(unittest):

    def teststring(self):
        self.firstdeck = code.deck
        self.player1 = code.player(self.firstdeck[0, 1, 2, 10, 11])
        self.player2 = code.player(self.firstdeck[3, 4, 12, 13, 14])
        self.player3 = code.player(self.firstdeck[5, 6, 7, 15, 16])
        self.player4 = code.player(self.firstdeck[8, 9, 17, 18, 19])
        self.team1 = code.team(self.player1, self.player3, 0)
        self.team2 = code.team(self.player2, self.player4, 0)
        self.assertEqual(self.team1, f"Player1 cards: {self.team1.player1},\n Player2 cards: {self.team1.player2},\n Score: {self.team1.score}")