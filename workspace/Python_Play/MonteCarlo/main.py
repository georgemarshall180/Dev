import BettorTypes
import Games
import matplotlib as plt

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

# create a singleton to collect statistics on games.
class stat_collector(Singleton):
    '''
    def stat_collector(name, value):
    # collect the data
    stats = {}
    if repr(name) in stats:
        print('in stats current value is:' + stats[name])
        currvalue = stats[name]
        stats[name] = currvalue + value
        print("new stats value is : " + stats[name])

    #if result has data
    return stats
    '''

def main():
    bank = 100
    wagers = 100
    wagerunit = 10
    wins = 0
    loses = 0
    push = 0
    x =0
    result = dict()
    even = 0
    odd = 0
    ## end_result = stat_collector('test', 0)


    while x <= wagers:

        # Game 1 Blackjack
        result = Games.blackJack()
        if result == 'win':
            wins = wins + 1
        elif result == 'lose':
            loses = loses + 1
        elif result == 'push':
            push = push + 1
        x = x + 1
        print("run:" + str(x))

    print("wins:" + str(wins))
    print("Loses:" + str(loses))
    print("Push:" + str(push))
    print("chance of winning:", wins/wagers)
    print("chance of loses:", loses/wagers)
    print("chance of push:", push/wagers)

    '''
    ## Game 2 Roulette
    ##
    mynumber = Games.roulette()
    result = Games.roulette()
    print('the winner is:' + repr(result))
    if result == mynumber:
        end_result.append(win, 1)
    elif result != mynumber:
        end_result.append(lose, 1)
    #if (result[0] %2) == 0:
        #even
        even =+ 1

    #elif result:
        #odd
        odd =+ 1


    ##    push = push + 1
    ## x = x + 1
    # print("run:" + str(x))
    '''

    ## game3 = Games.craps()


    ## game4 = Games.oddsgame(.5)


    ## while (wagers > 0) and (bank >0):
    ##    game

    plt.plot(result)
    plt.ylabel('')
    plt.xlabel(' ')
    plt.show()

# This runs main if this file is main
if __name__ == "__main__":
    main()