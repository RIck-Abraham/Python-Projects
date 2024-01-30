def swap_values(user_val1, user_val2):
    return user_val2, user_val1

if __name__ == '__main__': 
    first_num = int(input())
    sec_num = int(input())
    
    swap_num = swap_values(first_num, sec_num)
    print(*swap_num)
