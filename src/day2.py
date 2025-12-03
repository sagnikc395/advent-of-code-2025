import re
from typing import SupportsAbs

def check_invalid_id_pattern(number_string):
    pattern = r"^(\d+)\1$"

    if re.match(pattern,number_string):
        return True
    return False 



def solve_part1(id_ranges):
    summ = 0 
    for item in id_ranges:
        ids = item.split('-')
        firstId = int(ids[0])
        lastId = int(ids[1])
        for i in range(firstId,lastId+1):
            if check_invalid_id_pattern(str(i)):
                summ += i

    return summ

def check_invalid_id_pattern2(number_string):
    length = len(number_string)

    # iterate through possible lengths for the repeating subsequence
    for l_s in range(1,length // 2 + 1):
        if length % l_s == 0:
            subsequence = number_string[:l_s]
            k = length // l_s

            # check if the original string is exaclty 'subsequence' repeated
            if subsequence * k == number_string:
                return True
    return False


def solve_part2(id_ranges):
    summ = 0
    for item in id_ranges:
        ids = item.split('-')
        firstId = int(ids[0])
        lastId = int(ids[1])

        for i in range(firstId,lastId+1):
            if check_invalid_id_pattern2(str(i)):
                summ += i

    return summ 


def main():
    with open('../data/day2-input.txt','r') as f:
        content = f.read().strip().split(",")

    print(f"Part1 solution: {solve_part1(content)}")

    print(f"Part2 solution: {solve_part2(content)}")
    
        
        

if __name__ == '__main__':
    main()
