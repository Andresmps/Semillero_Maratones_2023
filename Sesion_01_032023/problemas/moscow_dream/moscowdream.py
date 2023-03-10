import sys

def convert_list_str_to_int(_list):
    return list(map(int, _list))

# It works with EOF inputs
def read_lines():
    _input = sys.stdin.readlines()
    return _input

def read_line():
    _input = sys.stdin.readline()
    return _input


a, b, c, n = convert_list_str_to_int(
    read_line().split())

# -----------------------------------------
# Solución
_answer = "YES"\
    if ((a >= 1) and (b >= 1) and (c >= 1)\
        and (a + b + c >= n)\
        and (n >= 3))\
    else "NO"

print(_answer)
# -----------------------------------------