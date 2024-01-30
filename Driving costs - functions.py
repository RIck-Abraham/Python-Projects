def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    return (driven_miles / miles_per_gallon) * dollars_per_gallon
    
if __name__ == '__main__':
    mpg = float(input())
    ppg = float(input())
    
    #10 miles
    cost_10 = driving_cost(10, mpg, ppg)
    print('{:.2f}'.format(cost_10))
    #50 miles
    cost_50 = driving_cost(50, mpg, ppg)
    print('{:.2f}'.format(cost_50))
    #400 miles
    cost_400 = driving_cost(400, mpg, ppg)
    print('{:.2f}'.format(cost_400))