# Write a Python program to assess if a file is closed or not

file = open("file1.txt", "r")
if file.closed:
    print("The file is closed")
else:
    print("The file is open")
file.close()
if file.closed:
    print("The file is closed")
else:
    print("The file is open")
