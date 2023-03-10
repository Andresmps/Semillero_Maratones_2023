import sys

def convert_list_str_to_int(_list):
    return list(map(int, _list))

# It works with EOF inputs
def read_lines():
    _input = sys.stdin.readlines()
    return _input

def iterate_over_input():
    _input = iter(read_lines())
    test_cases = next(_input)

    # for _ in range(len(test_cases)): Similar approach
    for line in _input:
        numb1, numb2 = (
            line.strip('\n')  # Remove leading whitespace/characters
                .split(' '))  # Split the string each time it founds the specify character: [.,_- ...]
        print(numb1, numb2)

_numerical_list = ["1", "2", "3", "4"]
print(convert_list_str_to_int(_numerical_list))
# Out:
# [1, 2, 3, 4]

# print(read_lines())
# In:
# 3
# 1 2
# 5 7
# 6 3

# Out:
# ['3\n', '1 2\n', '5 7\n', '6 3\n']

iterate_over_input()
# In:
# 3
# 1 2
# 5 7
# 6 3

# Out:
# 3
# 1 2
# 5 7
# 6 3
