def is_list_even(my_list):
    for index in range(len(my_list)):
        if (my_list[index] % 2 > 0):
            return False
    return True
    
def is_list_odd(my_list):    
    for index in range(len(my_list)):
        if (my_list[index] % 2 == 0):
            return False
    return True

if __name__ == '__main__':
    number_inputs = int(input())
    numbers = []
    
    for index in range(number_inputs):
        user_number = input()
        numbers.append(int(user_number))
            
    isEven = is_list_even(numbers)
    isOdd = is_list_odd(numbers)
    
    if (isEven is True) and (isOdd is False):
        print('all even')
    elif (isEven is False) and (isOdd is True):
        print('all odd')
    else:
        print('not even or odd')