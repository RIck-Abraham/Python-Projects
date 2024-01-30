user_string = input()
numbers = '0123456789'
criteria = False

for index in range(len(user_string)):
    if (numbers.find(user_string[index]) != -1):
        criteria = True
    else:
        criteria = False
        break
        
if (criteria is True):
    print('yes')
else:
    print('no')