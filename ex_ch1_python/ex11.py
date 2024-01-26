#!/usr/bin/env python3

def interleave(*lists):
    '''Interleave lists'''
    list1 = zip(*lists)
    result = []
    for i in list1:
        result.extend(i)
    
    return result

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c'])) # expected output: [1, 20, 'a', 2, 30, 'b', 3, 40, 'c']

if __name__ == "__main__":
    main()
