user_text = input()
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&','*','(',')','?']
count = 0

for index in range(len(user_text)):
    value = user_text[index]  # Retrieve value of element in list.
    if alphabet.count(value.upper()) > 0:
        count = count + 1
print(count) 