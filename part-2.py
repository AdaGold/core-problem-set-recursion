# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, querry):
    if not array:
        return False
    if querry == array[0]:
        return True
    return search(array[1:], querry)
# is_palindrome
def is_palindrome(s):
    if not s: # If the input string is empty, return False
        return False
    if len(s) <= 2 and s[0] == s[-1]:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
# digit_match
def digit_match(int1, int2):
    if int1 == int2:
        return len(str(int1))
    if int1 < 10 and int2 < 10 and int1 != int2:
        return 0
    if not int1 or not int2:
        return 0
    if int1 % 10 == int2 % 10:
        count = 1
    else:
        count = 0
    return count + digit_match(int1 // 10, int2 // 10)
