
import os
import time
start_time = time.perf_counter()

INPUT = os.path.dirname(__file__) + '/sample.txt'
INPUT = os.path.dirname(__file__) + '/input.txt'

def get_input_lines() -> list[str]:
    with open(INPUT, 'r') as fp:
        lines = [x.strip() for x in fp.readlines()]
    return [line for line in lines if line]

def get_input_sections() -> tuple[list[str], list[str]]:
    with open(INPUT, 'r') as fp:
        contents = fp.read()
    sec1, sec2 = contents.split('\n\n')
    return [x for x in sec1.split('\n') if x], [x for x in sec2.split('\n') if x]

def histogram(l: list[int|str]) -> dict[int|str, int]:
    result = {}
    for element in l:
        result.setdefault(element, 0)
        result[element] += 1
    return result


p1_result = 0
p2_result = 0

op_funcs = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '|': lambda x, y: int(str(x) + str(y)),
}

def evaluate(number_list: list[int], operators: str) -> tuple[bool, list[str]]:
    operand_stack = list(reversed(number_list))
    for operator in operators:
        left = operand_stack.pop()
        right = operand_stack.pop()
        new_value = op_funcs[operator](left, right)
        operand_stack.append(new_value)
    return operand_stack[-1]
    

def search(test_value: int, number_list: list[int], operators: str = '', part_2: bool = False) -> tuple[bool, list[str]]:
    current_val = evaluate(number_list, operators)
    if current_val == test_value and len(operators) == len(number_list) - 1:
        return True, number_list
    if current_val > test_value:
        return False, number_list
    if len(operators) == len(number_list) - 1:
        return False, number_list
    if part_2:
        works, number_list = search(test_value, number_list, operators + '*', part_2)
        if works:
            return works, number_list
    works, number_list = search(test_value, number_list, operators + '|', part_2)
    if works:
        return works, number_list
    return search(test_value, number_list, operators + '+', part_2)


lines = get_input_lines()
for eqn_number, line in enumerate(lines):
    test_value_str, number_list_str = line.split(': ', 1)
    test_value = int(test_value_str)
    number_list = [int(x) for x in number_list_str.split(' ')]
    solvable, solution = search(test_value, number_list)
    if solvable:
        print(f'equation {eqn_number} works!')
        p1_result += test_value
        p2_result += test_value
    else:
        solvable, solution = search(test_value, number_list, part_2=True)
        if solvable:
            p2_result += test_value


print(f'p1: {p1_result}')
print(f'p2: {p2_result}')
end_time = time.perf_counter()
print(f'Time: {end_time - start_time} s')
