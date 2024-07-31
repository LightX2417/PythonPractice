# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true


from collections import Counter

if __name__ == "__main__":

    s = input()
    s = sorted(s)

    letters = Counter(list(s))

    for k, v in letters.most_common(3):
        print(k, v)
