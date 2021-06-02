# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not len(array):
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def search(array, query):
    if not len(array):
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)


# digit_match
# I felt like I was super close on this one
# but I am missing something. Would love 
# to discuss this in our 1:1 (if time)
def digit_match(x, y):
    matches = 0

    if x % 10 ==  y % 10:
        matches +=1
        return matches

    if x//10 == 0 or y//10 == 0:
        return matches

    return digit_match(x //10, y //10)


