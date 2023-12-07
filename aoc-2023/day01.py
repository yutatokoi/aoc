# Grab contents of the textfile

# For every line of text:
# 1. Check first character
# 2. If it's a number, assign it to variable "digit1"
# 3. Else remove the first character
# 4. Repeat 1~3 until the first number is found
# 5. Complete steps 1~4 but starting from the last character,
#    assigning the number to variable "digit2"
# 6. Concatenate digit1 and digit2 to "two_digit_num"
# 7. Add two_digit_num to a list
# 8. If digit2 is not found, digit2 = digit1

input = open("day01-input.txt", "rt")

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def first_number():
    index = 0
    while index < len(line):
        if line[index] in numbers:
            first_digit = line[index]
            break
        index = index + 1

def second_number():
    index = len(line) - 1
    while index >= 0:
        if line[index] in numbers:
            print(line[index]) 
            break
        index = index - 1

# for line in input:
#     character = line[0]
#     if character in numbers:
#         print(character)
#     else:
#         print("Length: " + str(len(line)))

total_sum = 0

for line in input:
    index = 0
    while index < len(line):
        if line[index] in numbers:
            first_digit = line[index]
            break
        index = index + 1

    index = len(line) - 1
    while index >= 0:
        if line[index] in numbers:
            second_digit = line[index]
            break
        index = index - 1

    two_digit_num = int(first_digit + second_digit)
    
    total_sum = total_sum + two_digit_num

input.close()

print(total_sum)
