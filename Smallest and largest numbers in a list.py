number = int(input())
num_list = []
i = 0
j = 0
max = 0
min = 0


#Checks for greater than zero
while number > 0:
    #Create a list of numbers 
    num_list.append(number)
    number = int(input())   
    
    #Check for maximum
    for j in range(len(num_list)):
        if num_list[j] > max:
            max = num_list[j]   
            
    #Check for minimum
    min = num_list[i]
    for i in range(len(num_list)):
        if num_list[i] <= min :
            min = num_list[i]
            
print(min, max)
    