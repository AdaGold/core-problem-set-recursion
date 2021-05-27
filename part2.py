# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array_of_int,query_int_value):
    """
    Write a function search 

    that accepts an unsorted array of integers, 
    array,
    and an integer value to find, query. 

    It returns True 
    if query is found in array, 
    and False otherwise. 

    Make the algorithm recursive.
    """
    #base case 1
    if len(array_of_int) == 0:
        return False
    #base case 2
    if array_of_int[0] == query_int_value:  
        return True         #returns True if query is found in array
   
    #recursive
    result = search(array_of_int[1:], query_int_value)
    return result


# is_palindrome
def is_palindrome(text):
    """
    Write a recursive function is_palindrome 
    that accepts a string text as a parameter. 
    
    It returns a boolean value 
    indicating whether or not that string is a palindrome  .
    """
    # 1st base case, when properly nested string
    if len(text)==0:
        return True
    
    if len(text)==1:  #cover when just have 1 ")" left
        return True 

    right_side = text[-1]
    left_side = text[0]

    if left_side == right_side:
        result = is_palindrome(text[1:-1])   #recursion
        return result
    else:
        return False    #end early


# 3 digit_match
"""
Write a recursive function named digit_match. 
It accepts two non-negative integers as parameters. 

It returns the number of digits that match in the two integers.

Two digits match 
if they are equal 
and have the same position relative to the end of the number (i.e. starting with the ones digit).

In other words, 
the function should compare the last digits of each number, 
the second-to-last digits of each number, 
the third-to-last digits of each number, 
and so fort, 
counting how many pairs match.
"""
def digit_match(apples,oranges):
    #1 base case
    if apples == 0 and oranges == 0:
        return 1
    #2 base case
    elif apples <= 1 or oranges <= 1:
        return 0
    
    #recursdive
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
    else:
        return digit_match(apples // 10, oranges // 10) 


