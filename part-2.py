# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
# Write a function search that accepts an unsorted array of strings, array, and a string value to find, query. It returns True if query is found in array, and False otherwise. Make the algorithm recursive.

# Be sure to implement search using recursion.

# Here are the tests:

# def test_search_success_unsorted():
    # assert search(["b", "c", "a"], "a")


# def test_search_empty_array():
    # assert not search([], "a")


# def test_search_success_first_item():
    # assert search(["a", "b", "c"], "a")


# def test_search_not_found():
    # assert not search(["a", "b", "c"], "🌈")

def search(array, query):
    
    if not array:
        return False
    elif array[0] == query:
        return True
        
    return search(array[1:], query)



# is_palindrome
# Write a recursive function is_palindrome that accepts a string text as a parameter. It returns a boolean value indicating whether or not that string is a palindrome  .

# Input text	Return value
# "racecar"	True
# "raecar"	False
# Here are the tests:

# def test_is_palindrome_success():
    # assert is_palindrome("racecar")


# def test_is_palindrome_not_palindrome():
    # assert not is_palindrome("raecar")

def is_palindrome(text):
    
    if len(text) <= 1:
        return True
    
    return text[0] == text[-1] and  is_palindrome(text[1:-1])

# digit_match
# Write a recursive function named digit_match. It accepts two non-negative integers as parameters. It returns the number of digits that match in the two integers.

# Two digits match if they are equal and have the same position relative to the end of the number (i.e. starting with the ones digit).

# In other words, the function should compare the last digits of each number, the second-to-last digits of each number, the third-to-last digits of each number, and so fort, counting how many pairs match.

# Example:

# First number: 1072503891
# Second number: 62530841
# Number of matches: 4
# Matching pairs: 2-2, 5-5, 8-8, 1-1
# 1 0 7 2 5 0 3 8 9 1
    # | | | | | | | |
    # 6 2 5 3 0 8 4 1
# Here are the tests:
#
# d ef test_digit_match_large_inputs():
    # apples = 1072503891
    # oranges = 62530841
#
    # assert digit_match(apples, oranges) == 4


# def test_digit_match_no_matches():
    # apples = 0
    # oranges = 62530841

    # assert digit_match(apples, oranges) == 0


# def test_digit_match_clustered_matches():
    # apples = 841
    # oranges = 62530841

    # assert digit_match(apples, oranges) == 3


# def test_digit_match_single_digits():
    # apples = 0
    # oranges = 0

    # assert digit_match(apples, oranges) == 1


# def test_digit_match_small_inputs():
    # apples = 10
    # oranges = 20

    # assert digit_match(apples, oranges) == 1

def digit_match(apples, oranges):
    
    if apples < 10 or oranges < 10:
        
        if apples % 10 == oranges % 10:
            return 1
            
        return 0
        
    elif apples % 10 == oranges % 10:
        
        return 1 + digit_match(apples // 10, oranges // 10)
        
    return digit_match(apples // 10, oranges // 10)
