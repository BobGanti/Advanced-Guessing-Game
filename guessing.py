import random


# --- Setup --------------------------------------------- #
def isInteger(num, limit):
    try:
        if int(num) >= limit:
            return int(num)
    except ValueError:
        return None


def settings(num, text, limit):
    intNum = isInteger(num, limit)
    while intNum == None:
        print(f"Number should be +ve integer not less than {limit}!")
        intNum = isInteger(input(f"Enter {text} again (+ve integer not less than {limit}): "), limit)
    return intNum


def playGame():
    playerList = []
    scoreList = []
    startNum = settings(input("Enter start of random range (+ve integer): "), "start range", 0)
    endNum = settings(input(f"\nEnter end of random range (+ve integer above {startNum}): "), "end range", startNum + 1)
    numPlayers = settings(input("\nEnter number of Players (+ve integer above 0): "), "number of players", 1)

    for i in range(1, numPlayers + 1):
        # --- create surfix for i(example: if i=1, surfix = 1st; i=2, surfix = nd) ---#
        # surfix =(i==1)*"st" + (i==2)*"nd" + (i==3)*"rd" or "th"
        if i % 10 == 1:
            if i != 11:
                surfix = "st"
        elif i % 10 == 2:
            surfix = "nd"
        elif i % 10 == 3:
            surfix = "rd"
        else:
            surfix = "th"

        textDisplay = (numPlayers == 1) * "Name of player: " or f"Name of {i}{surfix} player: "
        player = input(textDisplay)

        playerList.append(player)
        scoreList.append(0)

    for i in range(len(playerList)):

        randomNumber = random.randint(startNum, endNum)
        print(f"\n{playerList[i]} IS PLAYING NOW")

        guessNumber = settings(input(f"Guess a number between {startNum} and {endNum} "), "number", startNum)

        while guessNumber != randomNumber:
            if (guessNumber < startNum):
                print(f"Out of Range Error! Your number cannot be less than {startNum}.")

            elif (guessNumber > endNum):
                print(f"Out of Range Error! Your number cannot be greater than {endNum}.")

            else:
                if (guessNumber > randomNumber):
                    print(guessNumber, "is high")

                if (guessNumber < randomNumber):
                    print(guessNumber, "is low")

                scoreList[i] += 1

            guessNumber = settings(input(f"\nGuess a number between {startNum} and {endNum} "), "number", startNum)

        print(f"{guessNumber} is the number. You Win!")
        print(f"Good job, {playerList[i]}")
    print("*" * 50)

    winnerList = []
    winningNum = min(scoreList)
    for i in range(len(scoreList)):
        if scoreList[i] == winningNum:
            winnerList.append(playerList[i])

    if len(winnerList) > 1:
        print("\nDRAW BETWEEN THE FOLLOWING:")
        for name in winnerList:
            print(name, end=" ")
    else:
        print(f"\nThe winner is {winnerList[0]}")

    print()
    for name, score in zip(playerList, scoreList):
        txt = (score > 1) * "guesses" or "guess"
        print(f"{name}: {score} wrong {txt}")


playGame()