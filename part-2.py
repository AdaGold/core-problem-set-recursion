# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    # base case: if empty then search return False
    if len(array) == 0:
        return False
    
    if array[0] == query:
         return True
    else :
        return search(array[1:], query)


# is_palindrome

def is_palindrome(text):
    #Base case
    if len(text) == 0: 
        return True
        
    if text[0] != text[-1]:
        return False
        
    return is_palindrome(text[1:-1])
        
        


# digit_match

def digit_match(x,y):
    #Basecase
    if x//10 == 0 or y//10 == 0:
        if x%10 == y%10:
            return 1
        else:
            return 0

        
    if x % 10 == y % 10:
        return 1 + digit_match(x//10, y//10)
    else:
        return digit_match(x//10, y//10)
