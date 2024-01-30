def steps_to_miles(user_steps):
    step_miles = 2000
    return user_steps / step_miles
    
if __name__ == '__main__':
    steps = float(input())
    miles = steps_to_miles(steps)
    print('{:.2f}'.format(miles))