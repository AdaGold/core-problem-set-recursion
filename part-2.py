# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if len(array) == 1:
        return array[0] == query
    elif len(array) == 0:
        return False
    if array[0] == query:
        return True
    array.pop(0)
    return search(array,query)
    


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False


# digit_match
def digit_match(n,k):
    if n == 0 and k == 0:
        return 1
    else:
        result = 0 
        if n == k%10 or k == n%10:
            return result+1
        elif n//10 == 0 or k//10 ==0:
            return result
        elif n%10 == k%10:
            result += 1    
        return result + digit_match(n//10,k//10)

