# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    
    n = len(array)
    if not n:
        return False
        
        #matches the first elem
    if array[0] == query:
        return True
        
    else:
        #slicing
        #starts at elem 1
        return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    
    n = len(text)
    
    if n <= 1:
        return True
        
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
        
        
    return False


# digit_match

def digit_match(num1, num2):
        #get the last digt using modulo
    num1_last_digit = num1 % 10
    num2_last_digit = num2 % 10
    
        #gets the remaining 
    qoutient_1 = num1 // 10
    qoutient_2 = num2 // 10
    
    
    if num1 == 0 and num2 == 0:
        return 1
        
    else:
        result = 0


    if num1_last_digit == num2_last_digit:
        result += 1
    if qoutient_1 == 0 or qoutient_2 == 0:
        return result
    
    return result + digit_match(qoutient_1, qoutient_2)
  
        
