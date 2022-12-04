filename = open("input.txt", "r").readlines()

# filename = open("input2.txt", "r").readlines()

# filename = open("inputTest.txt", "r").readlines()


def puzzle1(filename):
    sum = 0

    for line in filename:
        line = line.replace(" ", "").strip()
        range1 = line.split(",")[0]
        range2 = line.split(",")[1]

        range1FirstValue = int(range1.split("-")[0])
        range1SecondValue = int(range1.split("-")[1])

        range2FirstValue = int(range2.split("-")[0])
        range2SecondValue = int(range2.split("-")[1])

        listRange1 = list(range(range1FirstValue, range1SecondValue + 1))
        listRange2 = list(range(range2FirstValue, range2SecondValue + 1))

        check1 = all(item in listRange1 for item in listRange2)
        check2 = all(item in listRange2 for item in listRange1)

        if check1 is True or check2 is True:
            sum += 1

    return f"The total sum of puzzle1 is {sum}"


print(puzzle1(filename))


def puzzle2(filename):
    sum = 0

    for line in filename:
        line = line.replace(" ", "").strip()

        range1 = line.split(",")[0]
        range2 = line.split(",")[1]

        range1FirstValue = int(range1.split("-")[0])
        range1SecondValue = int(range1.split("-")[1])

        range2FirstValue = int(range2.split("-")[0])
        range2SecondValue = int(range2.split("-")[1])

        listRange1 = list(range(range1FirstValue, range1SecondValue + 1))
        listRange2 = list(range(range2FirstValue, range2SecondValue + 1))

        set_a = set(listRange1)
        set_b = set(listRange2)

        if (set_a & set_b):
            # just possible with sets
            sum += 1

    return f"The total sum of puzzle2 is {sum}"


print(puzzle2(filename))
