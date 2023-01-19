# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array == []:
        return False
    if array[-1] == query:
        return True
    
    return search(array[:-1], query)



# is_palindrome
def is_palindrome(text):
    
    if len(text) < 2:
        return True
    elif text[0] != text[-1]:
        return False
    
    
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    
    if num1 == 0 and num2 == 0:
        return 1
        
    def helper(n1, n2):
        if n1 == 0 or n2 == 0:    
            return 0
        
        if n1 % 10 == n2 % 10:
            return 1 + helper(n1 // 10 , n2 // 10)
        
        return helper(n1 // 10 , n2 // 10)
            
    return  helper(num1, num2)


