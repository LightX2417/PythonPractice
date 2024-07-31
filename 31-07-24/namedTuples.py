# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

from collections import namedtuple

n = int(input())
columns = input().split()
total_marks = 0
for _ in range(n):
    students = namedtuple("my_student", columns)
    MARKS, CLASS, NAME, ID = input().split()
    my_student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(my_student.MARKS)
print((total_marks / n))
