total_change_amount = int(input())

dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

#Determine if change is needed
if (total_change_amount < 1):
    print('No change')
else:
    #Count dollar bills
    if ((total_change_amount / 100) > 0):
        dollars = total_change_amount / 100
        if int(dollars) > 1:
            print(int(dollars),'Dollars')
        elif int(dollars) == 1:
            print(int(dollars), 'Dollar')
        total_change_amount = total_change_amount - (int(dollars) * 100)
    #Count quarters
    if ((total_change_amount / 25) > 0):
        quarters = total_change_amount / 25
        if int(quarters) > 1:
            print(int(quarters),'Quarters')
        elif int(quarters) == 1:
            print(int(quarters), 'Quarter')
        total_change_amount = total_change_amount - (int(quarters) * 25)
    #Count dimes
    if ((total_change_amount / 10) > 0):
        dimes = total_change_amount / 10
        if int(dimes) > 1:
            print(int(dimes),'Dimes')
        elif int(dimes) == 1:
            print(int(dimes), 'Dime')
        total_change_amount = total_change_amount - (int(dimes) * 10)
    #Count nickels
    if ((total_change_amount / 5) > 0):
        nickels = total_change_amount / 5
        if int(nickels) > 1:
            print(int(nickels),'Nickels')
        elif int(nickels) == 1:
            print(int(nickels), 'Nickel')
        total_change_amount = total_change_amount - (int(nickels) * 5)
    #Count pennies
    if ((total_change_amount / 1) > 0):
        pennies = total_change_amount / 1
        if int(pennies) > 1:
            print(int(pennies),'Pennies')
        elif int(pennies) == 1:
            print(int(pennies), 'Penny')
        total_change_amount = total_change_amount - (int(pennies) * 1)