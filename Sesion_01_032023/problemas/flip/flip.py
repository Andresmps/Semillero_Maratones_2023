import sys

def convert_list_str_to_int(_list):
    return list(map(int, _list))

def read_line():
    _input = sys.stdin.readline()
    return _input


# Solución
# -------------------------------------------------

A, B = convert_list_str_to_int( # Pasar los strings a enteros
    read_line()[::-1]  # Invierte la cadenas
    .split())
_A, _B = A, B

print(max(_A, _B))



# -------------------------------------------------