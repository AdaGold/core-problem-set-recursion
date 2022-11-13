# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 0 or len(text)==1:
        return True
    elif text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    if num1 == 0 and num2 == 0:
        return 1
    return digit_match_helper(num1, num2, 0)


def digit_match_helper(num1, num2, count):
    if num1 == 0 or num2 == 0:
        #done
        return count
    
    if num1 % 10 == num2 % 10:
        return digit_match_helper(num1 // 10, num2 // 10,count + 1)
    
    if num1 % 10 != num2 % 10:
        return digit_match_helper(num1 // 10, num2 // 10, count)


