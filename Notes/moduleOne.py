"""
<moduleOne.py>

-------------------------------------------------------------
Notes for CSE 2050 module one which covers:
- Python Basics
        * Statement                     
        * Values
        * Varibles                      
        * Comments
        * Docstrings                    
        * Data Types
        * Operators

        * Console Input/Output
        * Console Input/Output          * Sequence Slice
        * Operations on collections     * Functions
        * Modules                       * File Operations
        * Debugging                     * Exception handling
-------------------------------------------------------------

Author: Lorenzo .S
Contributors: [" "]
Created: 01-20-2026
Last Updated: 01-23-2026

"""

x = None

#=== Statement ===#
def statement(): #This is a function
    """
    Definition: A statement is the smallest unit of code a Interpreter can execute.
    Statements in Python are excuted in an ordered sequence top to bottom
    
    """
    print("Hello, world!") # This is a statment
    x=1                    # This is a also a statment
    return x               # Yes even this is a statment


#=== Value ===#
def value():
    """
    Defintion: A value is one of the basic things a program works with, like a letter or a number.

    Values can be stored in varibles
    """
    x = 5       #5 is the value here
    y = 5*5     #These two values multiply to form a new value saved under y
    return x, y


#=== Type ===#
def type():
    """
    Defintion: a type signifies what class a specifc object belongs too
    """
    x = "Hello, World!"           # x contains a "string" that is the class "Hello, World!" is made from
    y = 7                         # y contains an "int" that is the class 7 is made from
    print(type("Hello, World!"))  # type() can be used to test the type of the object, the result here would be <class 'str'>
    x = isinstance(5,int)         # ininstance() tests wether the specifed object is of the specified class. x here would eqaul two   
    print(x)  # True
    return

#=== Varible ===#
def varible():
    """
    Defintion: a storage location paired with an ID that points to said location it has a name as well asigned when initailzed in python, values can be stored at these specifed locations

    Varibles store values!

    Rules of naming a varible:
        * It must start with a letter or underscore, but can’t start with a number.
        * The remainder of the variable name may consist of letters, numbers and underscores.
        * Names are case sensitive
        * It can't be a key word

    Convetions:
        - It's a good practice to start the variables with a lowercase letter.
        - Use underscores to seperate multiple words in the varible name.
        - Varibles names should be descriptive.
    """
    color = "red"                       # color is the vairble name, the varible stores the string 'red' 
    age = 17                            # age is the varible name, the varible stores the int 17
    fruit = ['apple','pear']            # fruit is the varible name, the varible stores a list which contains the strings 'apple' and 'pear'

    return color,age,fruit

#=== Object ===#




#---- 01-23-2026 Lecuture Notes ----#

# - Atomic Data Types - #
def atomic_data_types():
     int = 5          # int
     float = 3.4      # float
     boolean = True   # boolean

# Atomic data types are Immutable

# You can not use indexes to access specific part of unordered objects because they are unordered

# Keys in dictionaries always need to be immutable objects

# - Slicing - #
def slicing():
        L = [1,2,3,4,5]

        print(L[0:2])   # First element is included last is excluded
        print(L[-1])    # Prints last element in the list
        print(L[0:4:2]) # Prints elements 0-4 and skips over every secound element

        return

# The diffrent between is and ==, == compares the values of two objects, while is compares the objects themselves

def print_min_max(L): 
        x = str(min(L)) 
        y = str(max(L)) 
        return x, y

L=[5,10]

print(print_min_max(L))








"""
Module One Notes

Data Structures

Stacks: 
        - Certain items one by one on top of eachother. 
        - New items get put on top, items have to be deleted top down.
        - Abstract data type with its own fucntionality


List: 
        - Abstract Data structure 

Python is object oreitned 


Statemnets:
        - The smallest unit of code a interpreter can execute
        EX: print("hello world") is a statement

Values:
        - Values basically just data
        EX: x = 5 is a value

Type:
        - The type of value a value is
        EX: is it a string, is it an in etc
        EX: x = "Hello World" x is a string object
        EX: x = isinstance(5,int) 

Everything in python is an object, it is inherentally object oreinted

Varibles:
        - a storage loctaion for a certain value
        - x = 5, 5 is the value, x is the varible
        - Naming convetions:
            * Must start with small leter or underscore
            * Names are case sensitive


Objects:
        - An instance of a class with unique attributes

Imutable vs Mutable
    - Imuntable items can not have their values changed, Modifying them makes a new object with a new id (ints,floats, strings,tuples)
    - Mutable objects can have there values changed(lists, dictionaries, sets)

Every class, method and function should have a docstring!

"""