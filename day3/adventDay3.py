import string
# import numpy as np

filename = open("input.txt", "r").readlines()

# filename = open("input2.txt", "r").readlines()

# filename = open("inputTest.txt", "r").readlines()


values = dict()

for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1

for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27


def puzzle1(filename):
    totalSum = 0
    for line in filename:
        line = line.replace(" ", "").strip()
        lengthOfLine = len(line)
        lineBreak = int(lengthOfLine/2)
        firstHalf = line[0:lineBreak]
        secondHalf = line[lineBreak:lengthOfLine]
        commonLetter = ''.join(set(firstHalf).intersection(secondHalf))
        totalSum += values[commonLetter]

    return f"The total sum of values for puzzle 1 is {totalSum}"


print(puzzle1(filename))


def puzzle2(filename):
    totalSum = 0
    roundCount = 0
    for line in filename:
        line = line.replace(" ", "").strip()
        roundCount += 1
        if roundCount == 1:
            firstLine = line
        elif roundCount == 2:
            secondLine = line
        elif roundCount == 3:
            thirdLine = line

        if roundCount == 3:
            commonLetter = ''.join(set(firstLine).intersection(
                secondLine).intersection(thirdLine))
            totalSum += values[commonLetter]
            firstLine = 0
            secondLine = 0
            thirdLine = 0
            roundCount = 0
    return f"The total sum of values for puzzle 2 is {totalSum}"


print(puzzle2(filename))
