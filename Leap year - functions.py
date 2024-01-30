def is_leap_year(user_year):
 if (user_year % 100 != 0) and (user_year % 4 != 0) or (user_year % 100 == 0) and (user_year % 400 != 0):
     return False
 else:
     return True
 
 
if __name__ == '__main__':
    year = int(input())
    
    leap_year = is_leap_year(year)
    
    if (leap_year == True):
        print(year, 'is a leap year.')
    else:
        print(year, 'is not a leap year.')