# Write a Python function that takes two lists and returns True if they have at least one common member.


def common(l1, l2):
    for x in l1:
        if x in l2:
            return True
    return False


l1 = eval(input("Enter a list"))
l2 = eval(input("Enter a list"))
print(common(l1, l2))
