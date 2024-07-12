# Write a program to calculate the sum and average of the digits present in a string.


def sum_digit(str):
    sum = avg = c = 0
    for i in str:
        if i.isdigit():
            c += 1
            x = int(i)
            sum = sum + x
            avg = sum / c
    print("Sum:", sum, "and average:", avg)


a = input("\nEnter a string: ")
sum_digit(a)
