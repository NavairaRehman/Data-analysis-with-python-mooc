#!/usr/bin/env python3

def distinct_characters(L):
    """Returns a dictionary where each key is a word in L and its value is the number of distinct characters in that word."""
    dict1 = {}
    for i in L:
        b = i.split()
        a = set(*b)
        dict1[i] = len(a)
    
    return dict1

def main():
    print(distinct_characters(["check", "look", "try", "pop"])) # {'check': 4, 'look': 3, 'try': 3, 'pop': 2}

if __name__ == "__main__":
    main()
