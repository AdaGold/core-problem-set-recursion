# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query or search(array[1::], query):
        return True
    else:
        return False
    


# is_palindrome
def is_palindrome(string):
    if not string:
        return True
    if string[0] == string[-1] and is_palindrome(string[1:-1]):
        return True
    else:
        return False



# digit_match
def digit_match(num1, num2):
    if num1 % 10 == num2 % 10:
        count = 1 
        if num1//10 !=0 and num2//10 != 0:
            return count + digit_match(num1//10, num2//10)
        else:
            return count
    else:
        count = 0
        if num1//10 !=0 and num2//10 != 0:
            return count + digit_match(num1//10, num2//10)
        else:
            return count

