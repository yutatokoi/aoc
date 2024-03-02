import re

input = open("input.txt", "rt")

sum = 0

for line in input:
    game_id = re.search(r'e (\d+):', line)
    game_id = game_id.group(1)
    game_id = int(game_id)

    game_result = re.search(r":\s*(.*)", line)
    game_result = game_result.group(1)

    round_results = re.split(";", game_result)
    
    round_validity = []

    for round in round_results:

        rgb = []

        red_cubes = re.search(r"(\d+) red", round)

        if red_cubes == None:
            red_cubes = 0
            rgb.append(red_cubes)
        else:
            red_cubes = red_cubes.group(1)
            red_cubes = int(red_cubes)
            rgb.append(red_cubes)
        
        green_cubes = re.search(r"(\d+) green", round)

        if green_cubes == None:
            green_cubes = 0
            rgb.append(green_cubes)
        else:
            green_cubes = green_cubes.group(1)
            green_cubes = int(green_cubes)
            rgb.append(green_cubes)

        blue_cubes = re.search(r"(\d+) blue", round)

        if blue_cubes == None:
            blue_cubes = 0
            rgb.append(blue_cubes)
        else:
            blue_cubes = blue_cubes.group(1)
            blue_cubes = int(blue_cubes)
            rgb.append(blue_cubes)

        if rgb[0] <= 12 and rgb[1] <= 13 and rgb[2] <= 14:
            round_validity.append(True)
        else:
            round_validity.append(False)

    # print(round_validity)

    if all(round_validity):
        sum = sum + game_id
    else:
        sum = sum

print(sum)

input.close()



### Part 2 ###

import re

input = open("input.txt", "rt")

sum = 0

for line in input:
    game_id = re.search(r'e (\d+):', line)
    game_id = game_id.group(1)
    game_id = int(game_id)

    game_result = re.search(r":\s*(.*)", line)
    game_result = game_result.group(1)

    round_results = re.split(";", game_result)
    
    numerical_game_results = []
    
    fewest_cubes = []

    for round in round_results:

        rgb = []

        red_cubes = re.search(r"(\d+) red", round)

        if red_cubes == None:
            red_cubes = 0
            rgb.append(red_cubes)
        else:
            red_cubes = red_cubes.group(1)
            red_cubes = int(red_cubes)
            rgb.append(red_cubes)
        
        green_cubes = re.search(r"(\d+) green", round)

        if green_cubes == None:
            green_cubes = 0
            rgb.append(green_cubes)
        else:
            green_cubes = green_cubes.group(1)
            green_cubes = int(green_cubes)
            rgb.append(green_cubes)

        blue_cubes = re.search(r"(\d+) blue", round)

        if blue_cubes == None:
            blue_cubes = 0
            rgb.append(blue_cubes)
        else:
            blue_cubes = blue_cubes.group(1)
            blue_cubes = int(blue_cubes)
            rgb.append(blue_cubes)

        numerical_game_results.append(rgb)
    
    all_red_cubes = []
    for i in range(len(numerical_game_results)):
        all_red_cubes.append(numerical_game_results[i][0])
    
    red_cube_min = max(all_red_cubes)

    all_green_cubes = []
    for i in range(len(numerical_game_results)):
        all_green_cubes.append(numerical_game_results[i][1])

    green_cube_min = max(all_green_cubes)

    all_blue_cubes = []
    for i in range(len(numerical_game_results)):
        all_blue_cubes.append(numerical_game_results[i][2])

    blue_cube_min = max(all_blue_cubes)

    power = red_cube_min * green_cube_min * blue_cube_min
    
    sum = sum + power

print(sum)

input.close()
