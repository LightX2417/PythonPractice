# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):
    array = set(array)
    avg = sum(array) / len(array)
    return f"{avg:.3f}"


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
