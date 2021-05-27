# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    if query == array[0]:
        return True
    else:
        return search(array[1:], query)


# is_palindrome

def is_palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True
    elif str[0] == str[-1:]:
        return is_palindrome(str[1:-1]) 
    return False

# digit_match


def digit_match(num1,num2):
    if num1 == 0  and num2 == 0:
        return 1
    elif (num1 < 10) or (num2 < 10):
        return 1 if (num1 % 10 == num2 % 10) else 0
        
    if num1 % 10 == num2 % 10:
        return digit_match(num1//10, num2//10) + 1
    else:
        return digit_match(num1//10, num2//10)

## is it normal our code looks so similar to the hints?
## as in, are these particularly easy recursive functions 
## or do they all typically function kind of the the same way
## so there's not a lot of variation in the form? 