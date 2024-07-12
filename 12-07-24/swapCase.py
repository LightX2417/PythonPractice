# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true


def swap_case(s):
    newString = "".join([x.capitalize() if x.islower() else x.lower() for x in s])
    return newString


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
