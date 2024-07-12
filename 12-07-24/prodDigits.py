# Write a function prodDigits() that inputs a number and returns the product of digits of that number.

def prodDigits(num):
    prod = 1
    while num:
        prod *= num % 10
        num //= 10
    return prod


n = int(input("Enter Number: "))
print(f"Products of the digits of {n} = {prodDigits(n)}")
