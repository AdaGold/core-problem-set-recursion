# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0]==query:
        return True
    
    return search(array[1:],query)
    
# is_palindrome

def is_palindrome(text):
    if len(text)<=1:
        return True
    
    return text[0]==text[-1] and is_palindrome(text[1:-1])

# is_palindrome_challenge
# 
def is_palindrome(text):
    text=text.lower()
    left=0
    right=len(text)-1

    return helper_function(text, left, right)

def helper_function(text, left, right):    
    if left>=right:
        return True
    
    return text[left]==text[right] and helper_function(text, left+1, right-1)    


# digit_match

def digit_match(apples,oranges):
    if apples<10 or oranges<10:
        return int(apples%10==oranges%10)

    return int(apples%10==oranges%10)+digit_match(apples//10,oranges//10)
    
