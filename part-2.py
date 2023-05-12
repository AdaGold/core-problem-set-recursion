# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,integer):
    while len(array) > 0:
        if array[0] == integer:
            return True
        return search(array[1:], integer)
    if not array:
        return False
    


# is_palindrome
def is_palindrome(text):
    if not text:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    if len(str(num1)) == 0 or len(str(num2)) == 0:
        return 0
    
    while len(str(num1)) >= 1 and len(str(num2)) >= 1:
        num1 = str(num1)
        num2 = str(num2)
        if num1[-1] == num2[-1]:
            return 1 + digit_match(num1[:-1],num2[:-1])
        return digit_match(num1[:-1],num2[:-1])

