# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search (unsorted,target):
    if len(unsorted) == 0:
        return False
    if unsorted[0] == target:
        return True
    return search(unsorted[1:], target)


# is_palindrome
def is_palindrome(text):
    if len(text) == 0:
        return True
    elif text[:1] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1,num2):
    if num1 == 0 and num2 == 0:
        return 1
    else:
        return digit_match_helper( num1, num2, 0 )
        

def digit_match_helper( num1, num2, count ):
    if num1 == 0 or num2 == 0:
        return count
    else:
        if num1 % 10 == num2 % 10:
            count += 1
        return digit_match_helper( num1 // 10, num2 // 10, count )

