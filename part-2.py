# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array )== 0 or not isinstance(query,str):
        return False
    if array[0] == query:
        return True
    else:
        array.pop(0)
        return search(array, query)


# is_palindrome
def is_palindrome(text):
    if len(text)<1:
        return True
    if text[0] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    # if both numbers are 0, return 1
    if num1==0 and num2==0:
        return 1
    # if one of the numbers is zero, 
    # that means we have reached end of that number
    if num1==0 or num2==0:
        return 0
    # if the number cannot be further divided further, 
    # return 0
    if num1//10 ==0 and num2//10==0:
        return 0
    # if the last digit of num1 equals num2,
    # return 1 + divide num1 and num2 by 10 and check those numbers
    if int(num1 % 10) == int(num2 %10):
        return 1 + digit_match(num1//10, num2//10)
    else:
        return 0 + digit_match(num1//10, num2//10)

