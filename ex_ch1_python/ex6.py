#!/usr/bin/env python3
'''
Exercise 6.
Write two functions: triple and square. Function triple multiplies its parameter by three. Function square raises its parameter to the power of two. For example, we have equalities triple(5)==15 and square(5)==25.

Part 1.
In the main function write a for loop that iterates through values 1 to 10, and for each value prints its triple and its square. The output should be as follows:

triple(1)==3 square(1)==1
triple(2)==6 square(2)==4
...
Part 2.
Now modify this for loop so that it stops iteration when the square of a value is larger than the triple of the value, without printing anything in the last iteration.
'''
def triple(a):
    return a*3

def square(a):
    return a**2

def main():
    for i in range(1,11):
        a = square(i)
        b = triple(i)
        if a > b:
            break
        print(f"triple({i})=={b}",f"square({i})=={a}")

if __name__ == "__main__":
    main()
