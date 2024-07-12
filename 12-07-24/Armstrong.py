# Write a function cubesum() that accepts an integer and returns the sum of the cubes of individual digits of that number.
# Use this function to make functions PrintArmstrong() and isArmstrong() to print Armstrong numbers and to find whether is an Armstrong number.


def cubesum(num):
    sum = 0
    while num:
        sum += pow(num % 10, 3)
        num = num // 10
    return sum


def isArmstrong(num):
    if num == cubesum(num):
        return True
    else:
        return False


def PrintArmstrong(n):
    for x in range(n + 1):
        if isArmstrong(x):
            print(x)


n = int(input("Enter a number: "))
if isArmstrong(n):
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")
print(f"Armstrong Numbers upto {n}")
PrintArmstrong(n)
