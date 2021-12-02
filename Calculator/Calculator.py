# Create a string with spaces proportional to a cosine of x in degrees
# def make_dot_string(x):
#    rad = radians(x)                             # cos works with radians
#   numspaces = int(20 * cos(radians(x)) + 20)   # scale to 0-40 spaces
#   st = ' ' * numspaces + 'o'                   # place 'o' after the spaces
#   return st
# Numbers 0 to 9
# Clear Value
# BackSpace
# Multiply,Divide,Minus,Plus

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def multiply(i, j):
    st = i * j
    return st


def divide(i, j):
    st = i / j
    return st


def minus(i, j):
    st = i - j
    return j


def plus(i, j):
    st = i + j
    return st


def main():
    x = "1.1"
    y = "2"

    if is_int(x) and is_int(y):
        print(multiply(int(x), int(y)))
    elif is_float(x) or is_float(y):
        print(multiply(float(x), float(y)))


main()
