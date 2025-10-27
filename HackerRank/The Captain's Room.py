# https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
elements = [int(x) for x in input().split()]

dictionary = {}

for el in elements:
    dictionary[el] = dictionary.get(el, 0) + 1

for key, value in dictionary.items():
    if value != k:
        print(key)

# input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
