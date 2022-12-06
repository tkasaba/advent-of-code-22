filename = open("input.txt", "r").readlines()

for line in filename:
    line = line.replace(" ", "").strip()

startingLength = len(line)


def puzzle1(line):
    testString = ""

    while len(line) != 0:
        for character in line:
            if len(testString) < 4:
                if character not in testString and len(testString) < 4:
                    testString += character
                else:
                    testString = ""
                    line = line[1:]
                    break
            else:
                result = startingLength - len(line) + 4
                print(len(line))
                line = ""
                break

    return f"The start-of-packet marker (puzzle1)  is {result}"


print(puzzle1(line))


def puzzle2(line):

    testString = ""

    while len(line) != 0:
        for character in line:
            if len(testString) < 14:
                if character not in testString and len(testString) < 14:
                    testString += character
                else:
                    testString = ""
                    line = line[1:]
                    break
            else:
                result = startingLength - len(line) + 14
                line = ""
                break

    return f"The start-of-message marker (puzzle2) is {result}"


print(puzzle2(line))
