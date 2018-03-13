import random


## This is each of the games that may be played. Start to put in rules to the games. Then see if you win or lose the game.
##
def rollDie():
    return random.randint(1,6)

def roulette_spin():
    numbers = {0: 'green', 00: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
               8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black',
               14: 'red', 15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red',
               22: 'black', 23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black',
               30: 'red', 31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}

    choice = random.randint(0,30)
    return choice, numbers[choice]

def chooseCard():
    return random.randint(1,11)

def blackJack():
    # print('BlackJack')
    result = ''

    # Create3 a hand for dealer and player.
    playercards = list()
    dealercards = list()

    # Deal the cards into the hand of each.
    playercards.append(chooseCard())
    playercards.append(chooseCard())
    dealercards.append(chooseCard())
    dealercards.append(chooseCard())

    # keep total of the cards to see how close they are.
    sumplayercards = sum(playercards)
    sumdealercards = sum(dealercards)

    # basic strategy if the player is 16 or less then hit unless over 21.
    while sumplayercards <= 16  :
        # keep hitting until you are up to 16
        playercards.append(chooseCard())
        sumplayercards = sum(playercards)

        # see if you bust
        if sumplayercards > 21:
            result = 'lose'
            return result

    # deal to the Dealer until he hits 17 or more
    while sumdealercards <= 17 :
        # keep hitting on dealer until it is 17 or higher
        dealercards.append(chooseCard())
        sumdealercards = sum(dealercards)

        #if the dealer busts
        if sumdealercards > 21:
            result = 'win'
            # print(result)
            return result
        # dealer wins on 21
        elif sumdealercards == 21:
            result = 'lose'
            # print(result)
            return result

    # See if you won or lost.
    # if the players cards are higher than dealers you win
    if sumplayercards > sumdealercards:
        result = 'win'
        return result
    # if the dealer and player have same they push.
    if sumplayercards == sumdealercards:
        result = 'push'
        return result
    # if the player is less than the dealer but neither has busted.
    if sumplayercards < sumdealercards:
        result = 'lose'
        return result

    ## bets
    ## double down
    ## split
    ## insurance

    return result

def roulette():
    # print("Roulette")
    result = roulette_spin()
    print("Number is:" + repr(result) )

    ## BETS
    ## 1-12,12-24,24-36
    ## 1-18, 18-36
    ## black or red
    ## even or odd
    return result

def craps():
    print("craps")
    die.append(rollDie())
    die.append(rollDie())

    return die

def oddsgame(odds):
    print('odds game')
    result  = odds * 1
    return result