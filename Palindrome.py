# Needs to be corrected
# Try statistics & evil is alive


def changeWord(word):
    changed_word = word
    # Count the number of times the character occurs in the word
    num_occurrences = word.count(" ")

    # Remove the appropriate position(s) in word string.
    position = +1
    for occurrence in range(num_occurrences):
        position = changed_word.find(" ", position) # Find the position of the next occurrence
        changed_word = changed_word[:position] + changed_word[position + 1:] # Rebuild the word string
        
    return changed_word
    
def checkWord(newWord):
    i = len(newWord) * -1
    # Reverse the word
    rev_word = ""
    for index in range(len(newWord)):
        rev_word = rev_word + newWord[i]
        i = i + 1
    if (rev_word == newWord):    
        answer = 'is a palindrome'
    else:
        answer = 'is not a palindrome'
    
    return answer
    
phrase = input()
noSpaces = changeWord(phrase)
palindrome = checkWord(noSpaces)

print(phrase, palindrome)