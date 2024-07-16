# Write a program to generate 100 random lottery tickets (each lottery number must be 10 digits long) and pick two lucky tickets from it as a winner.

import random

tickets = ["".join(str(random.randint(0, 9)) for x in range(10)) for i in range(100)]
winners = random.sample(tickets, k=2)
print(f"The winners are:\n{winners[0]}\n{winners[1]}")
