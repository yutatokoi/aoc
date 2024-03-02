file = open('input.txt', 'r', encoding='utf-8')

total_sum = 0

for line in file:

    i = 0
    tens_digit = 0

    while i < len(line):
        try:
            int(line[i])
        except:
            i += 1
        else:
            tens_digit = line[i]
            i = len(line)
    
    i = 0
    ones_digit = 0

    line = line[::-1]

    while i < len(line):
        try:
            int(line[i])
        except:
            i += 1
        else:
            ones_digit = line[i]
            i = len(line)

    calibration_value = int(tens_digit + ones_digit)
    total_sum += calibration_value

file.close()

print(total_sum)

### Part 2 ###

f = open('input.txt', 'r', encoding='utf-8')

total = 0

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for line in f:

    i = 0
    tens_digit = 0
    while i < len(line):
        if line[i] in digits:
            tens_digit = line[i]
            i = len(line)
        elif line[i] == 'o' and line[i + 1] == 'n' and line[i + 2] == 'e':
            tens_digit = '1'
            i = len(line)
        elif line[i] == 't' and line[i + 1] == 'w' and line[i + 2] == 'o':
            tens_digit = '2'
            i = len(line)
        elif line[i] == 't' and line[i + 1] == 'h' and line[i + 2] == 'r' and line [i + 3] == 'e' and line[i + 4] == 'e':
            tens_digit = '3'
            i = len(line)
        elif line[i] == 'f' and line[i + 1] == 'o' and line[i + 2] == 'u' and line [i + 3] == 'r':
            tens_digit = '4'
            i = len(line)
        elif line[i] == 'f' and line[i + 1] == 'i' and line[i + 2] == 'v' and line [i + 3] == 'e':
            tens_digit = '5'
            i = len(line)
        elif line[i] == 's' and line[i + 1] == 'i' and line[i + 2] == 'x':
            tens_digit = '6'
            i = len(line)
        elif line[i] == 's' and line[i + 1] == 'e' and line[i + 2] == 'v' and line [i + 3] == 'e' and line[i + 4] == 'n':
            tens_digit = '7'
            i = len(line)
        elif line[i] == 'e' and line[i + 1] == 'i' and line[i + 2] == 'g' and line [i + 3] == 'h' and line[i + 4] == 't':
            tens_digit = '8'
            i = len(line)
        elif line[i] == 'n' and line[i + 1] == 'i' and line[i + 2] == 'n' and line [i + 3] == 'e':
            tens_digit = '9'
            i = len(line)
        else:
            i += 1

    line = line[::-1]
    i = 0
    ones_digit = 0
    while i < len(line):
        if line[i] in digits:
            ones_digit = line[i]
            i = len(line)
        elif line[i] == 'o' and line[i - 1] == 'n' and line[i - 2] == 'e':
            ones_digit = '1'
            i = len(line)
        elif line[i] == 't' and line[i - 1] == 'w' and line[i - 2] == 'o':
            ones_digit = '2'
            i = len(line)
        elif line[i] == 't' and line[i - 1] == 'h' and line[i - 2] == 'r' and line [i - 3] == 'e' and line[i - 4] == 'e':
            ones_digit = '3'
            i = len(line)
        elif line[i] == 'f' and line[i - 1] == 'o' and line[i - 2] == 'u' and line [i - 3] == 'r':
            ones_digit = '4'
            i = len(line)
        elif line[i] == 'f' and line[i - 1] == 'i' and line[i - 2] == 'v' and line [i - 3] == 'e':
            ones_digit = '5'
            i = len(line)
        elif line[i] == 's' and line[i - 1] == 'i' and line[i - 2] == 'x':
            ones_digit = '6'
            i = len(line)
        elif line[i] == 's' and line[i - 1] == 'e' and line[i - 2] == 'v' and line [i - 3] == 'e' and line[i - 4] == 'n':
            ones_digit = '7'
            i = len(line)
        elif line[i] == 'e' and line[i - 1] == 'i' and line[i - 2] == 'g' and line [i - 3] == 'h' and line[i - 4] == 't':
            ones_digit = '8'
            i = len(line)
        elif line[i] == 'n' and line[i - 1] == 'i' and line[i - 2] == 'n' and line [i - 3] == 'e':
            ones_digit = '9'
            i = len(line)
        else:
            i += 1
    
    cal_num = 10 * int(tens_digit) + int(ones_digit) 
    total += cal_num

f.close()

print(total)

