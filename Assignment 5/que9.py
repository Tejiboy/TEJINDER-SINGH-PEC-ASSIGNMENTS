words = input("Enter a list of words separated by space: ").split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Number of occurrences of each word: ", word_count)
