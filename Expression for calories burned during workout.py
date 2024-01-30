''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
''' Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''

age = int(input())
weight = int(input())
heartRate = int(input())
time = int(input())

calories_woman = ((age * 0.074) - (weight * 0.05741) + (heartRate * 0.4472) - 20.4022) * time / 4.184
calories_man = ((age * 0.2017) + (weight * 0.09036) + (heartRate * 0.6309) - 55.0969) * time / 4.184

print('Women: {:.2f} calories'.format(calories_woman))
print('Men: {:.2f} calories'.format(calories_man))
