# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if len(array) == 0:
        return False
    elif query == array[0]:
        return True
    else:
        return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if text[0] != text[-1]:
        return False
    elif len(text) == 1:
        return True
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    if num1 == 0 and num2 == 0:
        return 1
    elif num1 < 10 or num2 < 10:
        if num1 % 10 == num2 % 10:
            return 1
        else:
            return 0
    
    if num1 % 10 == num2 % 10:
        return 1 + digit_match(num1 // 10, num2 // 10)
    else:
        return digit_match(num1 // 10, num2 // 10)

    # non-recursion solution (I couldn't figure out how to do it using recursion, so I did a non-recursion solution first.)
    
    # s1 = str(num1)[::-1]
    # s2 = str(num2)[::-1]
    # count = 0
    
    # if len(s1) < len(s2):
    #     length = len(s1)
    # else:
    #     length = len(s2)
        
    # for i in range(length):
    #     if s1[i] == s2[i]:
    #         count += 1
    # return count
