
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

DIRECTIONS = (
    (0, -1),  # UP
    (1, 0),   # RIGHT
    (0, 1),   # DOWN
    (-1, 0),  # LEFT
    (-1, -1),  # UP LEFT
    (1, -1),   # UP RIGHT
    (-1, 1),   # DOWN LEFT
    (1, 1),    # DOWN RIGHT
)
def inverse_dirs(direction: tuple[int, int]) -> list[tuple[int, int]]:
    return [
        (-direction[1], direction[0]),
        (direction[1], -direction[0]),
    ]


p1_result = 0
p2_result = 0

lines = get_input_lines()

def search(pos: tuple[int, int], direction: tuple[int, int], search_for: str) -> bool:
    for index, search_char in enumerate(search_for):
        new_pos = pos[0] + direction[0] * index, pos[1] + direction[1] * index
        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(lines[0]) or new_pos[1] >= len(lines):
            return False
        found_char = lines[new_pos[1]][new_pos[0]]
        if found_char != search_char:
            return False
    return True

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != 'X':
            continue
        for direction in DIRECTIONS:
            found = search((x, y), direction, 'XMAS')
            if found:
                p1_result += 1

mas_results = set()
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != 'M':
            continue
        for direction in DIRECTIONS:
            if 0 in direction:
                # only allow diagonals; + shapes don't count as x shapes apparently
                continue
            found = search((x, y), direction, 'MAS')
            if found:
                mas_results.add((x, y, direction))

cross_mases = 0
for x, y, direction in mas_results:
    for inverse_direction in inverse_dirs(direction):
        other_x = x + direction[0] - inverse_direction[0]
        other_y = y + direction[1] - inverse_direction[1]
        if (other_x, other_y, inverse_direction) in mas_results:
            cross_mases += 1
            print(f'{x, y} and {other_x, other_y} -- {direction}')

p2_result = cross_mases // 2


print(f'p1: {p1_result}')
print(f'p2: {p2_result}')
end_time = time.perf_counter()
print(f'Time: {end_time - start_time} s')
