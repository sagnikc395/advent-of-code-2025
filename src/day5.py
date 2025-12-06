import bisect 

def solve_part1(fresh_ingredients_ids, available_ingredient_ids):
    # fresh_ingredients_count = 0

    # def check_if_in_range(id,id_ranges):
    #     low,high = id_ranges.split('-')
    #     low = int(low)
    #     high = int(high)

    #     if id >= low and id <= high:
    #         return True
        
    #     return False 
    
    # idx = 0 
    # for id in available_ingredient_ids:
    #     if check_if_in_range(int(id),fresh_ingredients_ids[idx]):
    #         fresh_ingredients_count  += 1
    #     else:
    #         idx += 1

    # return fresh_ingredients_count
    fresh_ingredients_count = 0 
    fresh_ingredients_ids_ranges = []

    for id_ranges in fresh_ingredients_ids:
        low,high = id_ranges.split('-')
        low = int(low)
        high = int(high)
        fresh_ingredients_ids_ranges.append((low,high))
    
    available_ingredient_ids = [int(i) for i in available_ingredient_ids]

    #merge sort and binary search 
    fresh_ingredients_ids_ranges.sort()

    merged = []
    for start,end in fresh_ingredients_ids_ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start,end])
        else:
            merged[-1][1] = max(merged[-1][1],end)

    print(f"Merged ranges: {merged}")

    #querying and checking
    start_points = [r[0] for r in merged]

    for val in available_ingredient_ids:
        idx = bisect.bisect_right(start_points,val) - 1

        if idx >= 0:
            range_start, range_end = merged[idx]
            if range_start <= val <= range_end:
                fresh_ingredients_count += 1
    
    return fresh_ingredients_count



def main():
    with open("../data/day5-input.txt", "r") as f:
        p = f.read().strip()

    lines = p.split("\n")
    break_point = lines.index("")
    fresh_ingredients_ids, available_ingredient_ids = (
        lines[:break_point],
        lines[break_point + 1 :],
    )
    print("Part1 result: ")
    print(
        solve_part1(
            fresh_ingredients_ids=fresh_ingredients_ids,
            available_ingredient_ids=available_ingredient_ids,
        )
    )


if __name__ == "__main__":
    main()
