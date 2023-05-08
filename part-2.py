# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    try:
        if array[0] == query:
            return True
        return search(array[1:], query)
    
    except IndexError: return False


# is_palindrome
def is_palindrome(str):
    if len(str) < 2:
        return True
    if str[0] != str[-1]:
        return False
    return is_palindrome(str[1:-1])


# digit_match
def digit_match(num1, num2, count=0):
    num1, num2 = str(num1), str(num2)
    if len(num1) < 1 or len(num2) < 1:
        return count
    elif num1[-1] == num2[-1]:
        count += 1
    return digit_match(num1[:-1], num2[:-1], count)

