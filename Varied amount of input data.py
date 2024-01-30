sum = 0
avg = 0
i = 0
x = list(map(int, input().split())) 
while i < len(x):
    sum = sum + x[i]
    i = i + 1

avg = int(sum / i)
print(avg, max(x)) 