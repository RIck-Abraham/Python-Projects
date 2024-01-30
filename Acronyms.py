def getAcronym(name):
    acronym = name[0]
    
    # Count the number of times the character occurs in the word
    num_occurrences = name.count(" ")

    # Build the aconym.
    position = 1
    for occurrence in range(num_occurrences):
        position = name.find(" ", position) # Find the position of the next occurrence
        position = position + 1
        if name[position].isupper():
            acronym = acronym + name[position]
    
    return acronym
    

phrase = input()
print(getAcronym(phrase))