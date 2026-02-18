"""
<moduleThree.py>

-------------------------------------------------------------
Notes for CSE 2050 module three which covers:

-------------------------------------------------------------

Author: Lorenzo .S
Contributors: [" "]
Created: 01-28-2026
Last Updated: 01-28-2026

"""

# !!!! I NEED TO GO BACK AND TAKE BETTER NOTES ON THIS SECTION !!!! #


#=== Imports ===#
import unittest #Standard Library import




#---- 02-04-2026 Lecuture Notes ----#

def unittest():
    """
    import the unittest package in order to test your files

    Will create methods to test the behavoir of our code
    """

    pass

def test_driven_development():
    """
    Start with creating a bunch of test cases, run and fail cuz no code is written yet

    write code and pass all the tests

    refactor, remove all the fat
    """

# Private instances do not get tested via unittest

# Q: How do decided if your code is efficient?
# A: Time it takes for code to run, resources it takes to complete the task


# Thinking about effeicenty helps us develop good habits, intution and design descisons

# Measure effecinty: Measure time it takes for program to run, count the number of operations the program executes


def running_time():
    """
    Defintion: The number of atomic operrations is uesed to describe the running time of an algorithm

    Atomic Operations:
        * Atherimetic and boolean operations
        * Object Creation
        * Varible assignment
        * Branching
        * Calling a function
        * Returning from a function
    """
    y = 0 # Two atomic operations
    x = [j for i in range(1,10) for j in range(1,10)] # 81 atomic operations

    return x,y

"""
Chcking the running time of a fucntion

def f001(L):
    new list = []   # 2 operations, creation and assignment


"""

def asymptotic_order_of_growth():
    """
    Defintion: 
    """

    pass


def asymptotic_notation():
    """
    Definition: Used to describe the running time of an algorithm (how much time an algo takes given input n)


    """
    pass


def find_target(L,t):
    """

    Class room examples for Aysmototic order of growth

    """
    for i in L: #... n loops times
        if i == t: #... 2 operations, if and compare
            return True # ...  1 operation
    return False  # ...  1 operation

n = 10
L = [i for i in range (1,n+1)]
print(L)
find_target(L, 1)


# !!!! I NEED TO GO BACK AND TAKE BETTER NOTES ON THIS SECTION !!!! #

# In this lecture it was important to be able to know what time in Asymtotic notation a particular function ran in O(N+M) etc