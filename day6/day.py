
import os

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


p1_result = 0
p2_result = 0

DIRECTIONS = (
    (0, -1),  # UP
    (1, 0),   # RIGHT
    (0, 1),   # DOWN
    (-1, 0),  # LEFT
)

lines = get_input_lines()
height = len(lines)
width = len(lines[0])
obstacles = set()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '#':
            obstacles.add((x, y))
        elif char == '^':
            start_pos = (x, y)

def add(pos: tuple[int, int], d: tuple[int, int]) -> tuple[int, int]:
    return (pos[0] + d[0], pos[1] + d[1])

# Part 1
def simulate(start_pos: tuple[int, int], start_direction: int, obstacles: set[tuple[int, int]]):
    """return: loops, visited positions, visited states"""
    visited_positions = set()
    visited_states = set()
    pos = start_pos
    direction = start_direction
    while pos[0] >= 0 and pos[1] >= 0 and pos[0] < width and pos[1] < height:
        visited_positions.add(pos)
        if (pos, direction) in visited_states:
            return True, visited_positions, visited_states
        visited_states.add((pos, direction))
        pos, direction = step(pos, direction, obstacles)
    return False, visited_positions, visited_states

def step(pos: tuple[int, int], direction: int, obstacles: set[tuple[int, int]]) -> tuple[tuple[int, int], int]:
    new_pos = add(pos, DIRECTIONS[direction])
    if new_pos in obstacles:
        direction += 1
        if direction >= len(DIRECTIONS):
            direction -= len(DIRECTIONS)
        return pos, direction
    else:
        return new_pos, direction

loops, visited_positions, visited_states = simulate(start_pos, 0, obstacles)
assert not loops
p1_result = len(visited_positions)

p2_result = 0
print(f'{len(visited_positions)} visited positions')
# Note: This takes a good minute to run
for visited_position in visited_positions:
    if visited_position == start_pos:
        continue
    new_obstacles = obstacles.union([(visited_position)])
    loops, _, _ = simulate(start_pos, 0, new_obstacles)
    if loops:
        p2_result += 1

print(f'p1: {p1_result}')
print(f'p2: {p2_result}')
