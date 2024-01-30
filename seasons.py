input_month = input()
input_day = int(input())

days_in_month = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

spring = ['March', 'April', 'May', 'June']
summer = ['June', 'July', 'August', 'September']
autumn = ['September', 'October', 'November', 'December']
winter = ['December', 'January', 'February', 'March']

#Checks to meet parameters
if (input_month in days_in_month) and (input_day <= days_in_month[input_month]):
    #Spring
    if (input_month in spring):
        if (input_month == 'March') and (input_day < 20):
            print('Winter')
        elif (input_month == 'June') and (input_day > 20):
            print('Summer')
        else:
            if (input_day <= 0):
                print('Invalid')
            else:
                print('Spring')
    #Summer
    elif (input_month in summer):
        if (input_month == 'June') and (input_day < 21):
            print('Spring')
        elif (input_month == 'September') and (input_day > 21):
            print('Autumn')
        else:
            if (input_day <= 0):
                print('Invalid')
            else:
                print('Summer')
    #Autumn
    elif (input_month in autumn):
        if (input_month == 'September') and (input_day < 22):
            print('Summer')
        elif (input_month == 'December') and (input_day > 20):
            print('Winter')
        else:
            if (input_day <= 0):
                print('Invalid')
            else:
                print('Autumn')
    #Winter
    elif (input_month in winter):
        if (input_month == 'December') and (input_day < 21):
            print('Autumn')
        elif (input_month == 'March') and (input_day > 19):
            print('Spring')
        else:
            if (input_day <= 0):
                print('Invalid')
            else:
                print('Autumn')
    else:
        print('Error')
else:
    print('Invalid')