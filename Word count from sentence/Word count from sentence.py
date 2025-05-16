# Word Count Project

# Function to count the number of characters in a sentence.
def CountCharacters():
    print("Welcome to word count, where you can count the number of characters in a sentence.")
    
    # Taking input from the user and storing it in a variable.
    sentence = input("Enter the sentence/word: ")
    
    characters = 0
    
    # Looping through the sentence to count the number of characters.
    for i in sentence:
        characters += 1
    print("The number of characters in the sentence is: ", characters)  
    
    return characters

CountCharacters()
