import BettorTypes
import Games


def main():
    bank = 100
    wagers = 100
    wagerunit = 10
    wins = 0
    loses = 0
    push = 0
    x =0
    result = dict()


    while x <= wagers:

        wagers
        # print(Games.blackJack())
        # result = Games.blackJack()
        # print(Games.roulette())
        result = Games.roulette()
        print(result)

       ## if result == 'win':
        ##    wins = wins + 1
       ## elif result == 'lose':
        ##    loses = loses + 1
       ## elif result == 'push':
        ##    push = push + 1
       ## x = x + 1
        # print("run:" + str(x))

    # print("wins:" + str(wins))
    # print("Loses:" + str(loses))
    # print("Push:" + str(push))
    # print("chance of winning:", wins/wagers)
    # print("chance of loses:", loses/wagers)
    # print("chance of push:", push/wagers)




    ## game2 = Games.roulette()
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