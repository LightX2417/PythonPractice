# Write a Python program that takes a text file as input and returns the number of words of a given text file.

with open("file1.txt", "r") as file:
    word_count = 0
    for line in file:
        words = line.split()
        word_count += len(words)
    print(word_count)
