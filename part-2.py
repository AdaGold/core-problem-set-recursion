# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
        
    i = 0
    if array[i] == query:
        return True
        
    return search(array[i+1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 0:
        return True
        
    if text[0] != text[-1]:
        return False
        
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges, count=0):
    if apples % 10 == oranges % 10:
        count += 1
    
    if apples//10 == 0 or oranges//10 == 0:
        return count
        
    return digit_match(apples//10, oranges//10, count)

