def exact_change(user_total):
    total_change_amount = user_total
    
    #Count dollar bills
    if ((total_change_amount / 100) > 0):
        dollars = int(total_change_amount / 100)
        total_change_amount = total_change_amount - (int(dollars) * 100)
    else:
        dollars = 0
    #Count quarters
    if ((total_change_amount / 25) > 0):
        quarters = int(total_change_amount / 25)
        total_change_amount = total_change_amount - (int(quarters) * 25)
    else:
        quarters = 0
        
    #Count dimes
    if ((total_change_amount / 10) > 0):
        dimes = int(total_change_amount / 10)
        total_change_amount = total_change_amount - (int(dimes) * 10)
    else:
        dimes = 0
        
    #Count nickels
    if ((total_change_amount / 5) > 0):
        nickels = int(total_change_amount / 5)
        total_change_amount = total_change_amount - (int(nickels) * 5)
    else:
        nickels = 0
    #Count pennies
    if ((total_change_amount / 1) > 0):
        pennies = int(total_change_amount / 1)
        total_change_amount = total_change_amount - (int(pennies) * 1)
    else:
        pennies = 0

    return dollars, quarters, dimes, nickels, pennies
    
if __name__ == '__main__': 
    input_val = int(input())
    if (input_val < 1):
        print('no change')
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
        
        #Print Dollars
        if int(num_dollars) > 1:
            print(int(num_dollars),'dollars')
        elif int(num_dollars) == 1:
            print(int(num_dollars), 'dollar')
        
        #Print Quarters
        if int(num_quarters) > 1:
            print(int(num_quarters),'quarters')
        elif int(num_quarters) == 1:
            print(int(num_quarters), 'quarter')
            
        #Print Dimes
        if int(num_dimes) > 1:
            print(int(num_dimes),'dimes')
        elif int(num_dimes) == 1:
            print(int(num_dimes), 'dime')
                
        #Print Nickels
        if int(num_nickels) > 1:
            print(int(num_nickels),'nickels')
        elif int(num_nickels) == 1:
            print(int(num_nickels), 'nickel')
            
        #Print Pennies
        if int(num_pennies) > 1:
            print(int(num_pennies),'pennies')
        elif int(num_pennies) == 1:
            print(int(num_pennies), 'penny')