#!/usr/bin/env python3

def transform(a, b):
    """Returns a list where each element is the product of the elements in a and b at the same index."""
    l1 = map(int,a.split())
    l2 = map(int,b.split())
    
    
    L = zip(l1,l2)
    
    return(list(map(lambda x : x[0]*x[1],L)))

def main():
    a = "1 5 3"
    b = "2 6 -1"
    print((transform(a, b)))

if __name__ == "__main__":
    main()
