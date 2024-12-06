
import os

# INPUT = os.path.dirname(__file__) + '/sample.txt'
INPUT = os.path.dirname(__file__) + '/input.txt'

def get_input_lines() -> list[str]:
    with open(INPUT, 'r') as fp:
    # with open(os.path.dirname(__file__) + '/input.txt', 'r') as fp:
        lines = fp.readlines()
    return [line for line in lines if line]

def get_input_sections() -> tuple[list[str], list[str]]:
    with open(INPUT, 'r') as fp:
    # with open(os.path.dirname(__file__) + '/input.txt', 'r') as fp:
        contents = fp.read()
    sec1, sec2 = contents.split('\n\n')
    return [x for x in sec1.split('\n') if x], [x for x in sec2.split('\n') if x]


lines = get_input_lines()
left = [int(x.split('   ', 1)[0]) for x in lines]
right = [int(x.split('   ', 1)[1]) for x in lines]

p1_result = 0
p2_result = 0

for x, y in zip(sorted(left), sorted(right)):
    p1_result += abs(x - y)


right_histogram = {}
for r in right:
    right_histogram.setdefault(r, 0)    
    right_histogram[r] += 1

for x in left:
    p2_result += right_histogram.get(x, 0) * x

print(f'p1: {p1_result}')
print(f'p2: {p2_result}')
