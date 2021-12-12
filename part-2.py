# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if len(array)==0:
        return False
    elif query.isalpha() == False:
        return False
    elif array[0]== query:
        return True
    elif array[len(array)-1] == query:
       return True
    else:
        return False


# is_palindrome
def is_palindrome(text):
    return text == text[::-1]


# digit_match
def digit_match(apples,oranges, matches=0):
    if apples == 0 and oranges == 0:
        return matches +1
    elif apples< 10 or oranges < 10:
        if apples % 10 == oranges %10:
            return matches +1
        else:
            return matches
            
    elif apples %10 == oranges %10:
        return digit_match(apples // 10,oranges // 10, matches +1)
    else:
        return digit_match(apples//10,oranges//10,matches)

