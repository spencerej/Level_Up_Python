
word = input("Please give me a word: ")

word = word.replace(" ", "")

print(word)


    # punctuation marks
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # traverse the given string and if any punctuation
    # marks occur replace it with null
for x in word.lower():
    if x in punctuations:
        word = word.replace(x, "")
 
    # Print string without punctuation
print(word)


word_length = len(word)
step = 1
while step != word_length and step < word_length:
    if word[(step - 1)] == word[(-1 * step)]:
        step += 1
        print(step)
    else:
        print("That is not a palindrome! :(")
        exit()
else:
    print("That is a palindrome! :)")