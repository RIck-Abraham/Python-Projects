phrase = input()
rev_phrase = ""
i = 0
j = -1

#Checks to quit
while phrase != 'Quit' and phrase != 'quit' and phrase != 'q':
    #Reverse the string
    while i < (len(phrase)):
        rev_phrase = rev_phrase + phrase[j] 
        i = i + 1
        j = j - 1
    #print('Element {}: {}'.format(i, phrase))
    print(rev_phrase)
    #Next input
    rev_phrase = ""
    i = 0
    j = -1
    phrase = input()