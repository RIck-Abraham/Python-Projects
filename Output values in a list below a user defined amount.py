user_number1 = int(input())
numbers = []
low_numbers = []
value = 0

#Get the threshold index
threshold = user_number1

#Get the remaining numbers
for index in range(threshold+1):
    user_number2 = int(input())
    numbers.append(user_number2)
    
#Find the threshold value
for index in range(len(numbers)):
    if (numbers[index] == 100):
        value = 100
    else:
        value = numbers[threshold-1]
        
#Find lowest numbers
if (value == 100):
    for index in range(len(numbers)):
        if (numbers[index] < 100):
            print(numbers[index])
else:
    for index in range(len(numbers)):
        if (numbers[index] < value):
            print(numbers[index])
