### This file contains all the exercise questions for Chapter 1

## Exercise 1.1
### Write a program that uses a print statement to say 'hello world' as shown in 'Desired Output'.

## Exercise 1.2 
The program should ask the user for an input, and then print an answer as the examples below show.

What country are you from? Sweden
I have heard that Sweden is a beautiful country.

## Exercise 1.3
Make a program that gives the following output. You should use a for loop in your solution.

4 multiplied by 0 is 0
4 multiplied by 1 is 4
4 multiplied by 2 is 8
4 multiplied by 3 is 12
4 multiplied by 4 is 16
4 multiplied by 5 is 20
4 multiplied by 6 is 24
4 multiplied by 7 is 28
4 multiplied by 8 is 32
4 multiplied by 9 is 36
4 multiplied by 10 is 40

## Exercise 1.4
In the main function print a multiplication table, which is shown below:

   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100
For example at row 4 and column 9 we have 4*9=36.

Use two nested for loops to achive this.

## Exercise 1.5
Let us consider throwing two dice. (A dice can give a value between 1 and 6.) Use two nested for loops in the main function to iterate through all possible combinations the pair of dice can give. There are 36 possible combinations. Print all those combinations as (ordered) pairs that sum to 5. For example, your printout should include the pair (2,3). Print one pair per line.

## Exercise 1.6
In the main function write a for loop that iterates through values 1 to 10, and for each value prints its triple and its square. The output should be as follows:

triple(1)==3 square(1)==1
triple(2)==6 square(2)==4
...
Part 2.
Now modify this for loop so that it stops iteration when the square of a value is larger than the triple of the value, without printing anything in the last iteration.

## Exercise 1.7
Create a program that can compute the areas of three shapes, triangles, rectangles and circles, when their dimensions are given.

An endless loop should ask for which shape you want the area be calculated. An empty string as input will exit the loop. If the user gives a string that is none of the given shapes, the message “Unknown shape!” should be printed. Then it will ask for dimensions for that particular shape. When all the necessary dimensions are given, it prints the area, and starts the loop all over again. Use format specifier f for the area.

What happens if you give incorrect dimensions, like giving string "aa" as radius? You don't have to check for errors in the input.

## Exercise 1.8
Write a function solve_quadratic, that returns both solutions of a generic quadratic as a pair (2-tuple) when the coefficients are given as parameters.

## Exercise 1.9
Suppose we have two lists L1 and L2 that contain integers which are sorted in ascending order. Create a function merge that gets these lists as parameters and returns a new sorted list L that has all the elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). Do this using the fact that both lists are already sorted. You can’t use the sorted function or the sort method in implementing the merge method. You can however use these sorted in the main function for creating inputs to the merge function. Test with a couple of examples in the main function that your solution works correctly.

## Exercise 1.10
Create a function named detect_ranges that gets a list of integers as a parameter. The function should then sort this list, and transform the list into another list where pairs are used for all the detected intervals. So 3,4,5,6 is replaced by the pair (3,7). Numbers that are not part of any interval result just single numbers. The resulting list consists of these numbers and pairs, separated by commas. An example of how this function works:

print(detect_ranges([2,5,4,8,12,6,7,10,13]))
[2,(4,9),10,(12,14)]
Note that the second element of the pair does not belong to the range. This is consistent with the way Python's range function works. You may assume that no element in the input list appears multiple times.

## Exercise 1.11
Write function interleave that gets arbitrary number of lists as parameters. You may assume that all the lists have equal length. The function should return one list containing all the elements from the input lists interleaved. Test your function from the main function of the program.

Example: interleave([1,2,3], [20,30,40], ['a', 'b', 'c']) should return [1, 20, 'a', 2, 30, 'b', 3, 40, 'c']. Use the zip function to implement interleave. Remember the extend method of list objects.

## Exercise 1.12
Write function distinct_characters that gets a list of strings as a parameter. It should return a dictionary whose keys are the strings of the input list and the corresponding values are the numbers of distinct characters in the key.

Use the set container to temporarily store the distinct characters in a string. Example of usage: distinct_characters(["check", "look", "try", "pop"]) should return { "check" : 4, "look" : 3, "try" : 3, "pop" : 2}.

## Exercise 1.13
Make a function reverse_dictionary that creates a Finnish to English dictionary based on a English to Finnish dictionary given as a parameter. The values of the created dictionary should be lists of words. It should work like this:

d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
reverse_dictionary(d)
{'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}

## Exercise 1.14
Write function find_matching that gets a list of strings and a search string as parameters. The function should return the indices to those elements in the input list that contain the search string. Use the function enumerate.

An example: find_matching(["sensitive", "engine", "rubbish", "comment"], "en") should return the list [0, 1, 3].

## Exercise 1.15
Redo the earlier exercise which printed all the pairs of two dice results that sum to 5. But this time use a list comprehension. Print one pair per line.

## Exercise 1.16
Write a function transform that gets two strings as parameters and returns a list of integers. The function should split the strings into words, and convert these words to integers. This should give two lists of integers. Then the function should return a list whose elements are multiplication of two integers in the respective positions in the lists. For example transform("1 5 3", "2 6 -1") should return the list of integers [2, 30, -3].

You have to use split, map, and zip functions/methods. You may assume that the two input strings are in correct format.

## Exercise 1.17
Write a function positive_list that gets a list of numbers as a parameter, and returns a list with the negative numbers and zero filtered out using the filter function.

The function call positive_list([2,-2,0,1,-7]) should return the list [2,1]. Test your function in the main function.

## Exercise 1.18
Write function acronyms which takes a string as a parameter and returns a list of acronyms. A word is an acronym if it has length at least two, and all its characters are in uppercase. Before acronym detection, delete punctuation with the strip method.

## Exercise 1.19
Write a function sum_equation which takes a list of positive integers as parameters and returns a string with an equation of the sum of the elements.

Example: sum_equation([1,5,7]) returns "1 + 5 + 7 = 13" Observe, the spaces should be exactly as shown above. For an empty list the function should return the string "0 = 0".

## Exercise 1.20
Create your own module as file triangle.py in the src folder. The module should contain two functions:

hypotenuse which returns the length of the hypotenuse when given the lengths of two other sides of a right-angled triangle
area which returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.
Make sure both the functions and the module have descriptive docstrings. Add also the __version__ and __author__ attributes to the module. Call both your functions from the main function (which is in file usemodule.py).

## The End of Chapter 1 Exercises ##