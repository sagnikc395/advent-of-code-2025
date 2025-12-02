import os 
import math 

def solve_part1(contents):
    current_position = 50 
    zero_count = 0 

    for rotation in contents:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'L':
            current_position = (current_position - distance) % 100
        elif direction == 'R':
            current_position = (current_position + distance) % 100

        #check if new position is 0
        if current_position == 0 :
            zero_count += 1
        else:
            current_position = current_position
            zero_count = zero_count
    
    return zero_count

def calculate_zero_crossings(start_pos,direction,distance):
    if direction == 'R':
        crossings = math.floor((start_pos + distance) / 100)
    elif direction == 'L':
        crossings = math.floor((start_pos -1) / 100) - math.floor((start_pos - distance - 1) / 100)
    else:
        return 0
    
    return crossings

def solve_part2(contents):
    current_position = 50 
    total_zero_crossings = 0 

    for position in contents:
        direction = position[0]
        distance = int(position[1:])

        crossings_this_rotation = calculate_zero_crossings(current_position,direction,distance)
        total_zero_crossings += crossings_this_rotation

        if direction == 'L':
            current_position = (current_position - distance) % 100
        elif direction == 'R':
            current_position = (current_position + distance) % 100

    return total_zero_crossings
         


def main():
    current_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(current_path,"../data/day1-input.txt")
    with open(data_path) as f:
        contents = [i for i in f.read().strip().split("\n")]
    
    print(f"Part1 solution: {solve_part1(contents)}")
    print(f"Part2 solution: {solve_part2(contents)}")
    



if __name__ == '__main__':
    main()