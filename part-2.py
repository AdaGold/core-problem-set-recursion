# search
def search(array, query):
    if len(array) == 0:
        return False 
    if array[0] == query:
        return True    
    return search(array[1:], query)
    


# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    if len(text) == 2 and text[0] == text[-1]:
        return True    
    if text[0] != text[-1]:
        return False   
    return is_palindrome(text[1:-1])
    
    


# digit_match
def digit_match(num1, num2):
    if num1 < 10 or num2 < 10:
        if num1 % 10 == num2 % 10:
            return 1
        return 0
    if num1 % 10 == num2 % 10:  
        return 1 + digit_match(num1//10, num2//10)  
    else:
        return 0 + digit_match(num1//10, num2//10)
        

