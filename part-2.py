# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query, index=0):
    if not array or len(array) == index:
        return False
    
    return array[index] == query or search(array, query, index+1)


# is_palindrome
def is_palindrome(text, i=0):
    if len(text) < 1:
        return True
    if i == len(text)//2:
        return True
        
        
    j = len(text) - i - 1
    return text[i] == text[j] and is_palindrome(text, i+1)


# digit_match
def digit_match(apples, oranges ,count=0):
    a_r = apples % 10
    o_r = oranges % 10
    if a_r == o_r:
        count += 1
    
    new_apples = apples // 10
    new_oranges = oranges // 10
    if not new_apples or not new_oranges:
        return count
    return digit_match(new_apples, new_oranges ,count)

