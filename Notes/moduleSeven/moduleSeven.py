"""
<moduleSeven.py>

-------------------------------------------------------------
Notes for CSE 2050 module Seven which covers:

Module Topic: Divide and Conquer

Topics:
    * Chapter 13: Sorting with Divide and Conquer
        - Merge Sort
        - Quick Sort
    * Chapter 14: Selection
        - The quickselect algorithm
-------------------------------------------------------------

Author: Lorenzo .S
Contributors: [" "]
Created: 04-07-2026
Last Updated: 04-07-2026
"""


def divide_and_conquer():
    """
    Divide and Conquer is an algorithm design framework that boils down to breaking a big problem into smaller and smaller problems until those
    smaller problems are super easy to solve.

    There are 3(+1) parts of the Divide and Conquer framework which go as follows:
        1. Divide: This part is just dividing the big problem into sub problems
        2. Conquer: This step involves solving each sub problem.
        3. Combine: This step is where the solutions of each sub problem are combined to answer the original big problem
        +1. Base Case: These steps are recursive in nature, and with recursion there needs to be a base case to work towards.
                        The base case is usually met when subproblems are two small to be divided into smaller sub problems.


    Example of divide and conquer algorithm:

    Think about multiplying 26 by 25 in your head. Having to multiply these two big numbers can be kind of daunting on its own.
    Though what if we split up the problem into parts.

    instead of 26 times 25 let us use divide and conquer algorithm.

    Let's say we want to divide 25 into pieces equal to or smaller than 10.
    We can do this because multiplication can be done in any order as long as the factors add up to the original big factor example: (10 * 25) + (5*25) = 15 * 25

    So let us do that with 25
    1. Divide: 25 into 20 and 5 then divide 20 into 2 and 10 (technically the base case is divide numbers until the number is less than or equal to 10 here)
    2. Conquer: 25 * 5 = 125, 2 * 25 = 50, 10 * 25 = 250
    3. Combine: 125 + 50 + 250 = 425

    Now that is easier to do in your head because once you solve lets say 5 * 25, you do not have to hold that equation in your head, so that just becomes 125

    That is a practical way of thinking about divide and conquer algorithms.
    """

    example ="""
    Example of divide and conquer algorithm:
    
    Think about multiplying 26 by 25 in your head. Having to multiply these two big numbers can be kind of daunting on its own.
     However what if we split up the problem into parts?
    
    Instead of just 26 times 25 let us use divide and conquer framework.
    
    Let's say we want to divide 25 into pieces equal to or smaller than 10.
    We can do this because multiplication can be done in any order as long as the factors add up to the original big factor example: (10 * 25) + (5*25) = 15 * 25
    
    So let us do that with 25
    1. Divide: 25 into 20 and 5 then divide 20 into 2 and 10 (technically the base case is divide numbers until the number is less than or equal to 10 here)
    2. Conquer: 25 * 5 = 125, 2 * 25 = 50, 10 * 25 = 250
    3. Combine: 125 + 50 + 250 = 425
    
    Now that is easier to do in your head because once you solve lets say 5 * 25, you do not have to hold that equation in your head, so that just becomes 125
    
    That is a practical way of thinking about divide and conquer algorithms. """
    return print(example)

class MergeSort:

    def __init__(self, list) -> None:
        self.list = list
        return

    def merge_sort(self):
        pass

    def merge(self):
        pass


