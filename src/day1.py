import os 


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


def main():
    current_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(current_path,"../data/day1-input.txt")
    with open(data_path) as f:
        contents = [i for i in f.read().strip().split("\n")]
    
    print(solve_part1(contents))



if __name__ == '__main__':
    main()