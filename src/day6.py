from functools import reduce
import operator


def part1(operands, operators):
    part1_result = 0
    matrix = [list(map(int, s.split())) for s in operands]
    print(matrix)

    columns = zip(*matrix)

    for col, op_symbol in zip(columns, operators):
        if op_symbol == "+":
            op_func = operator.add
        elif op_symbol == "*":
            op_func = operator.mul
        else:
            continue

        result = reduce(op_func, col)
        part1_result += result

    return part1_result


def main():
    with open("../data/day6-input.txt", "r") as f:
        data = [i.strip() for i in f.read().split("\n") if i.strip()]

    operands = data[: len(data) - 1]
    operators = data[-1].split()

    print(f"Operands (Data Lines): {operands}")
    print(f"Operators: {operators}")

    print(f"Part1 results : {part1(operands=operands, operators=operators)}")


if __name__ == "__main__":
    main()
