# Write a program that gets a list of integers from input, and outputs non-negative 
# integers in ascending order (lowest to highest).  
# Output differs. See highlights below.
# Input
# -1 -7 -2 -88 5 -6
# Your output
# -88 -7 5 
# Expected output
# 5 


i = 0
sort = []
sort_num = ""
x = list(map(int, input().split())) 
while i < len(x):
    if (x[i] < 0):
        x.remove(x[i])
    i = i + 1
sort = x.sort()
print(*x, end = ' ')