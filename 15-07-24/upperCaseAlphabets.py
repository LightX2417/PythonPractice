# Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”.

with open("python.txt", "r") as file:
    count = 0
    for line in file:
        for char in line:
            if char.isupper():
                count += 1
    print(f"Number of uppercase alphabets: {count}")
