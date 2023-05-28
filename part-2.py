# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query): 
    if not array: 
        return False
    
    if array[0] != query: 
        array = array[1:]
        return search(array, query)
    else: 
        return True


# is_palindrome
def is_palindrome(text): 
    if not text or len(text) == 1: 
        return True
    
    if text[0] == text[-1]: 
        return is_palindrome(text[1:(len(text) -1)])
    else: 
        return False


# digit_match
def digit_match(num1, num2):
        
    if not num1 and not num2: 
        return 1
        
    else:
        result = 0
        last1 = num1 % 10 
        last2 = num2 % 10 
    
        if last1 == last2:
            result += 1
            
        if num1 // 10 == 0 or num2 // 10 == 0:
            return result
    
        return result + digit_match(num1 // 10, num2 // 10)

