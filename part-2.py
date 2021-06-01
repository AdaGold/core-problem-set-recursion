# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(arr, query):
    
    if not arr:
        return False
        
    if arr[0] != query:
        return search(arr[1:], query)

    return True


# is_palindrome
def is_palindrome(text):
    
    if not text:
        return True
        
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])

    return False


# digit_match
# referenced Chris' example after getting stuck
def digit_match(apples, oranges):
    
    if apples == 0 and oranges == 0:
        return 1 
        
    elif apples < 10 or oranges < 10: 
        if apples % 10 == oranges % 10: 
            return 1
        return 0
    
    if apples % 10 == oranges % 10: 
            return 1 + digit_match(apples // 10, oranges // 10) 
            
    return  digit_match(apples // 10, oranges // 10)

