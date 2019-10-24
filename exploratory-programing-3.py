import re

# Main function
def keywords(book):
    if type(book) != str:
         raise TypeError("Not a string")
    result = re.findall(r"\b[a-zA-Z]*at\b", book)
    threeWords = filter(lambda word: len(word) > 3, result)
    return threeWords
    #lambda is used to make anonymous functions
    #anonymous function is a function defined without a name
    #lambda can have many arguments but only one expression

# Opens a link to a text file
fPointer = open("Pride_and_Prejudice.txt", "r")

# Create variable for txt file contents
contents = fPointer.read()

# Close file link
fPointer.close()

print keywords(contents)
