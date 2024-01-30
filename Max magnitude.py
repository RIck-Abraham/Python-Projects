import math

def max_magnitude(user_val1, user_val2):
    if abs(user_val2) > abs(user_val1):
        return user_val2
    else:
        return user_val1

if __name__ == '__main__': 
    first_num = int(input())
    sec_num = int(input())
    
    lgMag = max_magnitude(first_num, sec_num)
    print(lgMag)
