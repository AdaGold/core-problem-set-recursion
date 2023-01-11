# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if not text:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match

def digit_match(apples, oranges): 
    if apples < 10 or oranges <10:
        if apples%10 == oranges%10:
            return 1
        return 0
    if apples%10 ==oranges%10:
        
        return 1+ digit_match(apples//10, oranges//10)
    return digit_match(apples//10, oranges//10)
