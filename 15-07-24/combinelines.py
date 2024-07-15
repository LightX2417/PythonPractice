# Write a Python program to combine each line from first file with the corresponding line in second file.

with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    for line1, line2 in zip(file1, file2):
        print(line1.strip() + " " + line2.strip())
