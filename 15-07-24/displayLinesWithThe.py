# Write a program to display all the lines in a file which have the word “the” in it.
with open('python.txt', 'r') as file:
   for line in file:
       if 'the' or 'The' in line:
           print(line)
