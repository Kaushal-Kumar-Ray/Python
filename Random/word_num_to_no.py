from word2number import w2n

# Take input from the user
word = input("Enter a number in words: ")

try:
    number = w2n.word_to_num(word)
    print("Output:",number)
except ValueError:
    print("Invalid input.")
