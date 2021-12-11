# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if array == []:
        return False
    if array[0] == query:
        return True
    x = array[0]
    array.remove(array[0])
    return search(array, query)

# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[:1] == text[-1:]:
        return is_palindrome(text[1:-1])
    else:
        return False

# digit_match
# note that this copies Kaida's code-along, as I had some issues
# I actually did get pretty close though!

def digit_match(x,y, matches=0):
    if x == 0 and y == 0:
        return matches + 1
    elif x < 10 or y < 10:
        if x % 10 == y % 10:
            return matches + 1
        else:
            return matches
    elif x % 10 == y % 10:
        return digit_match(x //10, y//10, matches +1)
    else:
        return digit_match(x // 10, y//10, matches)

