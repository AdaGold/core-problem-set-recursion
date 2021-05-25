# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query, i=0):
    if not array:
        return False
    elif array[i] == query:
        return True
    elif i == len(array)-1:
        return False
    else:
        return search(array, query, i+1)

# is_palindrome

def is_palindrome(text, left_i = 0):
    right_i = len(text) -1 -left_i
    if not text:
        return False
    elif left_i >= right_i:
        return True
    elif text[left_i] == text[right_i]:
        return is_palindrome(text, left_i + 1)

# digit_match

def digit_match(num1, num2):
    if num1 == 0 and num2 ==0:
        return 1
    elif num1 < 10 or num2 < 10:
        if num1%10 == num2%10:
            return 1
        return 0
    
    if num1 % 10 == num2 % 10:
        return 1+digit_match(num1//10, num2//10)

    return digit_match(num1//10, num2//10)

