#!/usr/bin/env python3

def sum_equation(lst):
    """Returns a string that represents a sum equation"""
    s = sum(lst)
    if s == 0:
        return "0 = 0"
    st = " + ".join(map(str,lst))
    return st + " = " + str(s)
def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
