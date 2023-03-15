import sys

def convert_list_str_to_int(_list):
    return list(map(int, _list))

def read_lines():
    _input = sys.stdin.readlines()
    return _input


# Solución
# -------------------------------------------------
# Ecuaciones
# a + b = s
# abs(a - b) = d -> a - b = d o b - a = d

# Restricciones
# a, b >= 0
# a, b deben ser enteros

# Resolviendo las ecuaciones:
# a = s + d / 2
# b = s - d / 2
# -------------------------------------------------

_input = read_lines()
_cases = int(_input[0])

for i in range(_cases):
    s, d = convert_list_str_to_int(
        _input[i + 1].split())

    a = (s + d) // 2
    b = (s - d) // 2

    if (d > s) or (a + b != s) or (a - b != d):
        print("impossible")
        continue

    print(f"{a} {b}")

# -------------------------------------------------