
import os
import time
import re
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

mul_pattern = re.compile(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))")
active = True
for line in lines:
    matches = re.findall(mul_pattern, line)
    for match in matches:
        if match[0] == 'do()':
            active = True
        elif match[0] == "don't()":
            active = False
        else:
            p1_result += int(match[1]) * int(match[2])
            if active:
                p2_result += int(match[1]) * int(match[2])

print(f'p1: {p1_result}')
print(f'p2: {p2_result}')

end_time = time.perf_counter()
print(f'Time: {end_time - start_time} s')
