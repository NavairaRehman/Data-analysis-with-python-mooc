#!/usr/bin/env python3

def positive_list(L):
    """Returns a list of positive numbers in L"""
    result = filter((lambda x : x > 0),L)
    return list(result)
def main():
    print(positive_list([2, -2, 0, 1, -7]))

if __name__ == "__main__":
    main()
