def getAcronym(name):
    acronym = name[0]  # Start the acronym with the first character of the name
    
    # Count the number of spaces in the name to determine the number of words
    num_occurrences = name.count(" ")

    # Initialize the position to start searching for the next word
    position = 1
    for occurrence in range(num_occurrences):
        position = name.find(" ", position)  # Find the position of the next space
        position += 1  # Move to the character after the space
        if position < len(name) and name[position].isupper():  # Check if the next character is uppercase and within the string bounds
            acronym += name[position]  # Add the uppercase character to the acronym
    
    return acronym

# Example usage
phrase = input("Enter a phrase: ")
print("The acronym is:", getAcronym(phrase))
