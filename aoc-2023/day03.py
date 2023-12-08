import re

input = open("day03-input.txt", "rt")

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['*', '/', '@', '&', '$', '=', '#', '-', '+', '%']

final_sum = 0

panel = []

for line in input:
    panel.append(list(line))

# y: y-th line of the input
# x: x-th character of the y-th line

for y in range(len(panel)):
    for x in range(len(panel[y])):
        print([x, y, panel[y][x]])

