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

