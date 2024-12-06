
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


orders, updates = get_input_sections()
rules: dict[set[int]] = {}
for order in orders:
    left, right = map(int, order.split('|'))
    rules.setdefault(left, set()).add(right)

def inconsistencies(pages: list[int], rules: dict[set[int]]) -> tuple:
    indices = {page: index for index, page in enumerate(pages)}
    assert len(indices) == len(pages)
    for index, page in enumerate(pages):
        nexts = rules.get(page, set())
        for next in nexts.intersection(indices):
            if indices[next] < index:
                return (index, indices[next])
    return ()


def swap(result, x, y):
    temp = result[x]
    result[x] = result[y]
    result[y] = temp


def reorder(pages: list[int], rules: dict[set[int]]) -> list[int]:
    indices = {page: index for index, page in enumerate(pages)}
    assert len(indices) == len(pages)
    problems = []
    for index, page in enumerate(pages):
        nexts = rules.get(page, set())
        for next in nexts.intersection(indices):
            if indices[next] < index:
                problems.append((index, indices[next]))
    result = pages.copy()
    for x, y in problems:
        swap(result, x, y)
    return result


p1_result = 0
p2_result = 0
for update_index, update in enumerate(updates):
    pages = [int(x) for x in update.split(',')]
    if not (i := inconsistencies(pages, rules)):
        print(f'Update {update_index}: okay')
        p1_result += pages[len(pages) // 2]
    else:
        while i:
            swap(pages, *i)
            i = inconsistencies(pages, rules)
        assert not inconsistencies(pages, rules)
        p2_result += pages[len(pages) // 2]

print(f'p1: {p1_result}')
print(f'p2: {p2_result}')
