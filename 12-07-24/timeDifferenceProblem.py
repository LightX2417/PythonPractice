# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true

import os
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    datetimeFormat = "%a %d %b %Y %H:%M:%S %z"
    t1Datetime = datetime.strptime(t1, datetimeFormat)
    t2Datetime = datetime.strptime(t2, datetimeFormat)
    return int(abs(t1Datetime - t2Datetime).total_seconds())


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + "\n")

    fptr.close()
