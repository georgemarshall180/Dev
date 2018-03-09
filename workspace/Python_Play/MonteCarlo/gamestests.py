import unittest
import Games
import BettorTypes


class Test_Casino_Games(unittest.TestCase):

    def setUp(self):
        # setup blackjack game
        game = self.blackJack()
        print(game)

    # player win
    def test_black_jack(self):
        while game != 'win' :
            game = self.blackJack()

        pcards = self.blackjack.playercards
        dcards = self.blackjack.dealercards

        if sum(pcards) > sum(dcards):
            self.assertEqual(True, False)
        return



    #player lose

    #player push

    #player bust

    # dealer bust



''' if __name__ == '__main__':
    unittest.main()
'''