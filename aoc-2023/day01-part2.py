input = open("day01-input.txt", "rt")

input2 = open("day01-input.txt", "rt")

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

total_sum = 0

for line in input:
    index = 0
    while index < len(line):
        if line[index] in numbers:
            first_digit = line[index] 
            break
        elif line[index] == "o":
            if line[index + 1] == "n" and line[index + 2] == "e":
                first_digit = "1"
                break
        elif line[index] == "t":
            if line[index + 1] == "w" and line[index + 2] == "o":
                first_digit = "2"
                break
            elif line[index + 1] == "h" and line[index + 2] == "r" and line[index + 3] == "e" and line[index + 4] == "e":
                first_digit = "3"
                break
        elif line[index] == "f":
            if line[index + 1] == "o" and line[index + 2] == "u" and line[index + 3] == "r":
                first_digit = "4"
                break
            elif line[index + 1] == "i" and line[index + 2] == "v" and line[index + 3] == "e":
                first_digit = "5"
                break
        elif line[index] == "s":
            if line[index + 1] == "i" and line[index + 2] == "x":
                first_digit = "6"
                break
            elif line[index + 1] == "e" and line[index + 2] == "v" and line[index + 3] == "e" and line[index + 4] == "n":
                first_digit = "7"
                break
        elif line[index] == "e":
            if line[index + 1] == "i" and line[index + 2] == "g" and line[index + 3] == "h" and line[index + 4] == "t":
                first_digit = "8"
                break
        elif line[index] == "n":
            if line[index + 1] == "i" and line[index + 2] == "n" and line[index + 3] == "e":
                first_digit = "9"
                break
        index = index + 1

    index = len(line) - 1
    while index >= 0:
        if line[index] in numbers:
            second_digit = line[index]
            break
        elif line[index] == "e":
            if line[index - 1] == "n" and line[index - 2] == "o":
                second_digit = "1"
                break
            elif line[index - 1] == "e" and line[index - 2] == "r" and line[index - 3] == "h" and line[index - 4] == "t":
                second_digit = "3"
                break
            elif line[index - 1] == "v" and line[index - 2] == "i" and line[index - 3] == "f":
                second_digit = "5"
                break
            elif line[index - 1] == "n" and line[index - 2] == "i" and line[index - 3] == "n":
                second_digit = "9"
                break
        elif line[index] == "o":
            if line[index - 1] == "w" and line[index - 2] == "t":
                second_digit = "2"
                break
        elif line[index] == "r":
            if line[index - 1] == "u" and line[index - 2] == "o" and line[index - 3] == "f":
                second_digit = "4"
                break
        elif line[index] == "x":
            if line[index - 1] == "i" and line[index - 2] == "s":
                second_digit = "6"
                break
        elif line[index] == "n":
            if line[index - 1] == "e" and line[index - 2] == "v" and line[index - 3] == "e" and line[index - 4] == "s":
                second_digit = "7" 
                break
        elif line[index] == "t":
            if line[index - 1] == "h" and line[index - 2] == "g" and line[index - 3] == "i" and line[index - 4] == "e":
                second_digit = "8"
                break
        index = index - 1
    
    two_digit_num = int(first_digit + second_digit)
    total_sum = total_sum + two_digit_num

input.close()

print(total_sum)

