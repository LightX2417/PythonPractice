# Write a function that takes in a list of integers and returns True if it contains 007 in order


def spy_game(numbers):
    seq = [0, 0, 7]
    i = 0
    for x in numbers:
        if x == seq[i]:
            i += 1
        if i == len(seq):
            return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
print(spy_game([0, 2, 5, 0, 9, 8, 7]))
print(spy_game([7, 2, 5, 0, 9, 8, 0]))
