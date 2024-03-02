import re

input = open("input.txt", "rt")

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['*', '/', '@', '&', '$', '=', '#', '-', '+', '%']

final_sum = 0

panel = []

for line in input:
    panel.append(list(line))

panel_with_coord = []
# y: y-th line of the input
# x: x-th character of the y-th line
for y in range(len(panel)):
    for x in range(len(panel[y])):
        panel_with_coord.append([x, y, panel[y][x]])

for i in range(len(panel_with_coord)):
    if panel_with_coord[i][2] in symbols:
        print("Top-left: " + str(panel_with_coord[i - 12]))
        print("Top-top: " + str(panel_with_coord[i - 11]))
        print("Top-right: " + str(panel_with_coord[i - 10]))
        print("Left: " + str(panel_with_coord[i - 1]))
        print("Right: " + str(panel_with_coord[i + 1]))
        print("Bottom-left: " + str(panel_with_coord[i + 10]))
        print("Bottom-bottom: " + str(panel_with_coord[i + 11]))
        print("Bottom-right: " + str(panel_with_coord[i + 12]))
