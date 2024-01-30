word = input()
password = ''

replacements = {
    'i': '!',
    'a': '@',
    'm': 'M',
    'B': '8',
    'o': '.',
}

for index in range(len(word)):
    value = word[index]  # Retrieve value of element in list.
    if value in replacements:
        password = password + replacements[value]
    else:
        password = password + value
print(password + 'q*s')