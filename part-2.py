# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if array == []:
        return False
    if array[len(array)-1] == query:
        return True
    array.pop()
    return search(array, query)

# is_palindrome

def is_palindrome(str):
    if len(str) < 2:
        return True
    if str[0] != str[-1]:
        return False
    return is_palindrome(str[1:-1])

# digit_match

def digit_match(num1, num2, matches=0):
    if num1 % 10 == num2 % 10:
        matches += 1
    if num1 // 10 and num2 // 10:
        return digit_match(num1 // 10, num2 // 10, matches)
    else:
        return matches
