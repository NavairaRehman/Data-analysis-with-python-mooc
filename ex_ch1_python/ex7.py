#!/usr/bin/env python3
'''
Exercise 7.
Create a program that can compute the areas of three shapes, triangles, rectangles and circles, when their dimensions are given.

An endless loop should ask for which shape you want the area be calculated. An empty string as input will exit the loop. If the user gives a string that is none of the given shapes, the message “Unknown shape!” should be printed. Then it will ask for dimensions for that particular shape. When all the necessary dimensions are given, it prints the area, and starts the loop all over again. Use format specifier f for the area.

What happens if you give incorrect dimensions, like giving string "aa" as radius? You don't have to check for errors in the input.
'''
import math

def circle_area(r):
    return math.pi * r**2

def rectangle_area(w,h):
    return w*h

def triangle_area(b,h):
    return b*h/2

def main():
    while(True):
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            b = float(input("Enter the base of the triangle: "))
            h = float(input("Enter the height of the triangle: "))
            area = triangle_area(b, h)
            print(f"The area is {area:.6f}")
        elif shape == "rectangle":
            w = float(input("Enter the width of the rectangle: "))
            h = float(input("Enter the height of the rectangle: "))
            area = rectangle_area(w, h)
            print(f"The area is {area:.6f}")
        elif shape == "circle":
            r = float(input("Enter the radius of the circle: "))
            area = circle_area(r)
            print(f"The area is {area:.6f}")
        elif shape == "":
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
