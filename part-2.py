# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if len(array) < 1:
        return False
    if array[-1] == query:
        return True
    return search(array[:-1], query)

# is_palindrome

def is_palindrome(text):
    
    
    left = text[0]
    right = text[-1]
    
    if left != right:
        return False
    
    if len(text) <= 1:
        return True

    return is_palindrome(text[1:-1])



# digit_match

def digit_match(apples, oranges):
    
    apples = str(apples)
    oranges = str(oranges)
    count = 0
    if len(apples) <= 1 or len(oranges) <= 1:
        if apples[-1] == oranges[-1]:
            count += 1
            return count
        else:
            return count
    if apples[-1] == oranges[-1]:
        count += 1
    return count + digit_match(apples[:-1],oranges[:-1])
