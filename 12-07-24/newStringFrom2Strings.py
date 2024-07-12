# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
# Sample String: 'Good', 'Morning'
# Expected Result: 'GgonoidnMor'

a = input("\nEnter first string: ")
b = input("Enter second string: ")
temp = ""
b = b[::-1]  # to reverse the string
length = len(a) if len(a) > len(b) else len(b)
for i in range(length):
    if i < len(a):
        temp += a[i]
    if i < len(b):
        temp += b[i]
print(temp)
