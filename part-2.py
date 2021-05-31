# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
        
    popped_letter = array.pop()
    if popped_letter == query:
        return True
    
    return search(array, query)



# is_palindrome
def is_palindrome(text):
    if len(text) == 0:
        return True
    
    if text[0] != text[-1]:
        return False
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])



# digit_match
def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
    if apples / 10 < 1 or oranges / 10 < 1:
        if apples % 10 == oranges % 10:
            return 1
        else:
            return 0
            
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples//10, oranges//10)
    else:
        return digit_match(apples//10, oranges//10)


