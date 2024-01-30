#Gets the number of values to check
numOfValues = int(input())

#Gets the numbers and puts them in an array
numbers = []
for index in range(numOfValues):
    userInput = int(input())
    numbers.append(userInput)
    
#Get the threshold
threshold = int(input())

#Find the lowest numbers and print
for index in range(len(numbers)):
    if (numbers[index] <= threshold):
        print(numbers[index])