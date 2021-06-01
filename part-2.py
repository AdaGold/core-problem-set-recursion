# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    elif query == array[-1]:
        return True
    return search(array[:-1], query)
    


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[:1] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2): 
    str1 = str(num1)
    str2 = str(num2)
    count = 0 

    if len(str1) == 0 or len(str2) == 0: 
        return count 
    elif str1[-1] == str2[-1]: 
        count += 1 
    return count + digit_match(str1[:-1], str2[:-1])

