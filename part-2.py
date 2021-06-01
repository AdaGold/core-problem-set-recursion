# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
"""
worked through the provided solution again!
My original solution didn't include recursion...
"""
# My initial solution
def search(array, query):
    if query in array:
        return True
    else:
        return False

# correct solution
"""
This solution checks if the first element is equal
to the provided query argument (when called).
If it's not equal to the query, it calls the function again-
but splices the array such that the array is one element shorter
when called recursively.
"""
def search(array, query):
    if not len(array):
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)

# is_palindrome
def is_palindrome(text):
    # if the string is either empty or 1 character, it is considered a palindrome
    if len(text) < 2:
        return True
    # if the first character in the string is not the same as the last
    # character, then it is not a palindrome.
    elif text[0] != text[-1]:
        return False
    # run the function (recursively), shortening the string (removing the
    # first character from the original given string, and running that
    # in the function until the base case(s) are met.)
    return is_palindrome(text[1:-1])


# digit_match
"""
the hint/example solution was really helpful.
It essential divides the given number by 2 and/or 3 and/or 5
as many times as possible. At the end of that division, the number
should equal 1 -because ugly numbers can only be divisible by 
those 3 prime factors. If it's not equal to 1, then we return
False. If it is equal to 1 at that point, we return True- it IS an ugly number.
"""
# provided solution
def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
    elif apples <= 1 or oranges <= 1:
        return 0
    
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
    else:
        return digit_match(apples // 10, oranges // 10)
