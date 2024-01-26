#!/usr/bin/env python3

def find_matching(L, pattern):
    """Returns a list of strings that contains pattern as a substring"""
    l1 = []
    for i,x in enumerate(L):
        if pattern in x:
            l1.append(i)
    return l1
def main():
    l1 = ['sensitive', 'engine', 'rubbish', 'comment']
    print(find_matching(l1,"t"))
    

if __name__ == "__main__":
    main()
