introstring=input("Welcome to the PYTHON WORLD!  Tell us how you feel about PYTHON:")
characterCount=0
wordCount=0
for letters in introstring:
    characterCount=characterCount + 1
    if (letters == " "):
        wordCount=wordCount + 1
        
print("Number of words:")
print(wordCount)
print("Number of letters:")
print(characterCount)
