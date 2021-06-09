# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    
    if not array:
        return False
    
    elif array[0] == query:
        return True
    
    else:
        return search(array[1:], query)


# is_palindrome

# def is_palindrome(text):
#     return text == text[::-1]

def is_palindrome(text):
    if len(text) < 2:
        return True
        
    elif text[0] != text[-1]:
        return False
        
    else:
        return is_palindrome(text[1:-1])

# digit_match

# def helper(str1, str2):
#     if len(str1) == 0 or len(str2) == 0:
#         return 0
        
#     last_apples = str1[-1]
#     last_oranges = str2[-1]
    
#     if last_apples == last_oranges:
#         return 1 + helper(str1[0:-1], str2[0:-1])
        
        
#     else:
#         return 0 + helper(str1[0:-1], str2[0:-1])
        

# def digit_match(apples, oranges):
#     return helper(str(apples), str(oranges))

def digit_match(apples, oranges):
    # Base cases:
    # If both apples and oranges are 0 return 1
    if apples == 0 and oranges == 0:
        return 1
    # If one or both are 1-digit numbers
    elif apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        
        return 0
    
    # Recursive Cases
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
        
    return digit_match(apples // 10, oranges // 10)
   
