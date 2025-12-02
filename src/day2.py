import re

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

def main():
    with open('../data/day2-input.txt','r') as f:
        content = f.read().strip().split(",")

    print(solve_part1(content))
    
        
        

if __name__ == '__main__':
    main()
