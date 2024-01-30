num_a = int(input())
num_b = int(input())
i = 0 
answer = []



if num_a > num_b:
    print("Second integer can't be less than the first.")
else:
    while (num_a <= num_b):
        answer.append(num_a)
        num_a = num_a + 10
        i = i + 1
    for index in range(len(answer)):
        value = answer[index]  # Retrieve value of element in list.
    print(*answer, '')