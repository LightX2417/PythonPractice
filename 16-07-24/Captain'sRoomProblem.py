# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

if __name__ == "__main__":
    k = int(input())
    rooms = list(map(int, input().split()))
    roomSet = set(rooms)
    roomSum = sum(rooms)
    roomSetSum = sum(roomSet) * k
    captainsRoom = (roomSetSum - roomSum) // (k - 1)
    print(captainsRoom)
