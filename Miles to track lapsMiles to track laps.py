def miles_to_laps(user_miles):
    lap_miles = 0.25
    return user_miles / lap_miles
    
    
if __name__ == '__main__':
    miles = float(input())
    num_laps = miles_to_laps(miles)
    print('{:.2f}'.format(num_laps))