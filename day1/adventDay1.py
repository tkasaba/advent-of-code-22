import numpy as np

filename = open ("/Users/tkasaba/bootcamp/python3Work/input.txt", "r").readlines() 

numberList = []
sum = 0
sumOfValues= []

for line in filename:
    if line.strip() == "":
        # print('The line is empty')
        numberList.append(line.strip())
    else:
        # print('The line is NOT empty', line)
        line =line.strip()
        numberList.append(int(line))

# print(numberList)

for number in numberList:
    if type(number) == int:
        sum+=number
    else:
        sumOfValues.append(sum)
        sum = 0
    
if number == numberList[-1]:
            sumOfValues.append(sum)


print (sumOfValues)
print(f"The maximum value is {max(sumOfValues)}")


sumOfValues.sort(reverse=True)
print(f"The sorted sumOfValues list is {sumOfValues}")

topThreeValues = sumOfValues[0] + sumOfValues[1] + sumOfValues[2]
print(f"The sum of the top 3 values is {topThreeValues}")


