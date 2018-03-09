

def martingale(previousResult, previousBet):
    ## this betting type doubles the bet after each loss. if you win then you drop back to original bet.
    ## streaks really create or lose this betting type. It can have high returns on short runs
    print("martingale")
    newbet = 0
    if previousResult == 'lose':
        newbet = previousBet*2
        return newbet
    elif previousResult == 'win':
        newbet = wagerunit
        return newbet
    return newbet


def simpleBetor(wagerunit):
    # bets the same amount each time.
    print("simple")
    newbet = wagerunit
    return newbet

def dalembert():
    # increases the bet by 1 unit every time lost and decrease bet by 1 unit every time won.
    ##
    return

def positiveProgression():
    # Every time you win, just add 50% to your bet. Start with $6. If you win then you'll add half of that, which is $3, 6+3=9
    # Whenever you lose, start over again with $6.
    return













