filename = open("input.txt", "r").readlines()
# filename = open ("input2.txt", "r").readlines()


def puzzle1(filename):

    opponentRock = "A"
    opponentPaper = "B"
    opponentScissors = "C"

    myRock = "X"
    myPaper = "Y"
    myScisscors = "Z"

    rock = 1
    paper = 2
    scissors = 3

    win = 6
    draw = 3
    lose = 0

    roundCount = 0
    myScore = 0
    myOpponentsScore = 0

    opponentTotalScore = 0
    myTotalScore = 0

    for line in filename:
        line = line.replace(" ", "").strip()
        roundCount += 1

        # print(f"Startinf round count {roundCount}")

        opponent = line[0]
        mine = line[1]

        if opponent == "A" and mine == "X":
            myScore += rock + draw
            myOpponentsScore += rock + draw

            # print(f"Draw Oponnent Score {myOpponentsScore}")
            # print(f"Draw My Score {myScore}")

        elif opponent == "B" and mine == "Y":
            myScore += paper + draw
            myOpponentsScore += paper + draw

            # print(f"Draw ponnent Score {myOpponentsScore}")
            # print(f"Draw My Score {myScore}")

        elif opponent == "C" and mine == "Z":
            myScore += scissors + draw
            myOpponentsScore += scissors + draw

            # print(f"Draw Oponnent Score {myOpponentsScore}")
            # print(f"Draw My Score {myScore}")

        elif opponent == opponentRock and mine == myScisscors:
            myScore += scissors + lose
            myOpponentsScore += rock + win

            # print(f"win Oponnent Score {myOpponentsScore}")
            # print(f"lose My Score {myScore}")

        elif opponent == opponentRock and mine == myPaper:
            myScore += paper + win
            myOpponentsScore += rock + lose

            # print(f"lose Oponnent Score {myOpponentsScore}")
            # print(f"win My Score {myScore}")

        elif opponent == opponentPaper and mine == myRock:
            myScore += rock + lose
            myOpponentsScore += paper + win

            # print(f"win Oponnent Score {myOpponentsScore}")
            # print(f"lose My Score {myScore}")

        elif opponent == opponentPaper and mine == myScisscors:
            myScore += scissors + win
            myOpponentsScore += paper + lose

            # print(f"lose Oponnent Score {myOpponentsScore}")
            # print(f"win My Score {myScore}")

        elif opponent == opponentScissors and mine == myRock:
            myScore += rock + win
            myOpponentsScore += scissors + lose

            # print(f"lose Oponnent Score {myOpponentsScore}")
            # print(f"win My Score {myScore}")

        elif opponent == opponentScissors and mine == myPaper:
            myScore += paper + lose
            myOpponentsScore += scissors + win

            # print(f"win Oponnent Score {myOpponentsScore}")
            # print(f"lose My Score {myScore}")

        if roundCount == 3:
            # print(roundCount)
            # print(f"Oponnent Total Score {opponentTotalScore}")
            # print(f"Oponnent Score {myOpponentsScore}")
            # print(f"My Total Score {myTotalScore}")
            # print(f"My Score {myScore}")
            opponentTotalScore += myOpponentsScore
            myTotalScore += myScore
            roundCount = 0
            myScore = 0
            myOpponentsScore = 0

    if roundCount != 0:
        opponentTotalScore += myOpponentsScore
        myTotalScore += myScore

    return f"Your total score for puzzle 1 is {myTotalScore}"


print(puzzle1(filename))


def puzzle2(filename):
    opponentRock = "A"
    opponentPaper = "B"
    opponentScissors = "C"

    lose = "X"
    draw = "Y"
    win = "Z"

    rock = 1
    paper = 2
    scissors = 3

    win = 6
    draw = 3
    lose = 0

    roundCount = 0
    myScore = 0
    myOpponentsScore = 0

    opponentTotalScore = 0
    myTotalScore = 0

    for line in filename:
        line = line.replace(" ", "").strip()
        roundCount += 1

        opponent = line[0]
        roundEnd = line[1]

        if roundEnd == "Y":
            if opponent == opponentRock:
                myScore += rock + draw
                myOpponentsScore += rock + draw
            elif opponent == opponentPaper:
                myScore += paper + draw
                myOpponentsScore += paper + draw
            elif opponent == opponentScissors:
                myScore += scissors + draw
                myOpponentsScore += scissors + draw
        elif roundEnd == "X":
            if opponent == opponentRock:
                myScore += scissors + lose
                myOpponentsScore += rock + win
            elif opponent == opponentPaper:
                myScore += rock + lose
                myOpponentsScore += paper + win
            elif opponent == opponentScissors:
                myScore += paper + lose
                myOpponentsScore += scissors + win

        elif roundEnd == "Z":
            if opponent == opponentRock:
                myScore += paper + win
                myOpponentsScore += rock + lose
            elif opponent == opponentPaper:
                myScore += scissors + win
                myOpponentsScore += paper + lose
            elif opponent == opponentScissors:
                myScore += rock + win
                myOpponentsScore += scissors + lose

        if roundCount == 3:
            # print(roundCount)
            # print(f"Oponnent Total Score {opponentTotalScore}")
            # print(f"Oponnent Score {myOpponentsScore}")
            # print(f"My Total Score {myTotalScore}")
            # print(f"My Score {myScore}")
            opponentTotalScore += myOpponentsScore
            myTotalScore += myScore
            roundCount = 0
            myScore = 0
            myOpponentsScore = 0

    if roundCount != 0:
        opponentTotalScore += myOpponentsScore
        myTotalScore += myScore

    return f"Your total score for puzzle 2 is {myTotalScore}"


print(puzzle2(filename))
