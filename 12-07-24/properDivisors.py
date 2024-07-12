# Write a function sumPdivisors() that finds the sum of proper divisors of a number. Proper divisors of a number are those numbers by which the number is divisible, except the number itself.

def sumPdivisors(num):
    sum = 0
    for x in range(1, num // 2 + 1):
        if num % x == 0:
            sum += x
    return sum


n = int(input("Enter Number: "))
print(f"Sum of the proper divisors of {n} = {sumPdivisors(n)}")
