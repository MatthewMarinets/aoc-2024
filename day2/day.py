
import os
import time
start_time = time.perf_counter()

INPUT = os.path.dirname(__file__) + '/sample.txt'
INPUT = os.path.dirname(__file__) + '/input.txt'

def get_input_lines() -> list[str]:
    with open(INPUT, 'r') as fp:
        lines = fp.readlines()
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

lines = get_input_lines()
reports = [[int(x) for x in line.split(' ')] for line in lines]

def unsafe_index(report: list[int]) -> int:
    if report[1] > report[0]:
        increasing = True
    else:
        increasing = False
    last = report[0]
    for index, item in enumerate(report[1:], 1):
        if item <= last and increasing:
            return index
        elif item >= last and not increasing:
            return index
        elif abs(item - last) > 3:
            return index
        last = item
    return 0

def is_dampened_safe(report: list[int]) -> bool:
    index = unsafe_index(report)
    if not index:
        return True
    elif unsafe_index(report[1:]) == 0:
        return True
    elif unsafe_index(report[:1] + report[2:]) == 0:
        return True
    elif unsafe_index(report[:index-1] + report[index:]) == 0:
        return True
    return unsafe_index(report[:index] + report[index+1:]) == 0


p1_result = len([report for report in reports if not unsafe_index(report)])
p2_safe = []
for report in reports:
    if is_dampened_safe(report):
        print('safe: ', end='')
        p2_safe.append(report)
    print(report)
p2_result = len(p2_safe)


print(f'p1: {p1_result}')
print(f'p2: {p2_result}')
end_time = time.perf_counter()
print(f'Time: {end_time - start_time} s')
