# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    elif array[0]==query:
        return True
    return search(array[1:],query)


# is_palindrome
def is_palindrome(text):
    if len(text)<2:
        return True
    if text[0]!=text[-1]:
        return False
    return is_palindrome(text[1:-1])



# digit_match
def digit_match(digit1,digit2):
    if digit1==0 and digit2==0: #edge case both are 0 and 1 digit
        return 1
    #if one or both are 1 digit
    elif digit1//10==0 or digit2//10==0:
        if digit1%10==digit2%10:
            return 1
        else:
            return 0
    
    elif digit1%10==digit2%10:
        return 1+digit_match(digit1//10, digit2//10)
    return digit_match(digit1//10, digit2//10)
        


