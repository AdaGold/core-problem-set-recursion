# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
"""Write a function search that accepts an unsorted array of integers, array, and an integer value to find, query. It returns True if query is found in array, and False otherwise. Make the algorithm recursive."""
#Non recursive solution O(N)
def search_non_rec(array, query):
    if query in array:
        return True
    return False
        
        
#Recursive solution
def search(array, query):
    #base case1, edge case
    if len(array) == 0:
        return False
    #base case 2
    if array[0] == query:
        return True
    #recursive case: slicing one element
    return search(array[1:], query)

# is_palindrome
"""Write a recursive function is_palindrome that accepts a string text as a parameter. It returns a boolean value indicating whether or not that string is a palindrome"""
def is_palindrome(text):
    #IndexError: string index out of range
    #base case #1
    if text[0] != text[-1]:
        return False
     #base case #2 for odd length str
    if len(text) < 2:
        return True
         
    #recursive case
    return is_palindrome(text[1:-1])

# digit_match
"""
Write a recursive function named digit_match. It accepts two non-negative integers as parameters. 
It returns the number of digits that match in the two integers.
Two digits match if they are equal and have the same position relative to the end of the number (i.e. starting with the ones digit).
"""
def digit_match(apples, oranges):
    #base case
    if apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        else:
            return 0
    #recursive case 1
    elif apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
    #recursive case 2
    else:
        return digit_match(apples // 10, oranges // 10)
    
    
#first approach -> not very recursive solution, but the logic is there
def digit_match_non_working(apples, oranges):
    a_index, o_index, match_pair = 0, 0, 0 #reinitialize index and match pair
    if len(str(apples)) < 1 or len(str(oranges)) < 1:
        return 0
    list1, list2 = str(apples), str(oranges)
    #less recursive way
    if list1[-1] == list2[-1] and a_index == o_index: 
        match_pair += 1
        a_index += 1
        o_index += 1
    
    return match_pair + digit_match(list1[:-1], list2[:-1])