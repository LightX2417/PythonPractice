# Write a Python program to count the frequency of words in a file.

with open("file1.txt", "r") as file:
    word_freq = {}
    for line in file:
        words = line.split()
        for word in words:
            if word.lower() not in word_freq:
                word_freq[word.lower()] = 1
            else:
                word_freq[word.lower()] += 1
    print(word_freq)
