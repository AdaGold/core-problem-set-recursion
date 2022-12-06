# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if len(array) == 0:
        return False
    else:
        if query in array[0]:
            return True
        else:
            return search(array[1:], query)

    




# is_palindrome
def is_palindrome(text):
    if len(text) < 1:
        return True
    else:
        if text[0] == text[-1]:
            return is_palindrome(text[1:-1])
        else:
            return False



# digit_match
def digit_match(first,second):
    first = str(first)
    second = str(second)
    count = 0
    if len(first) and len(second) > 0:
        if first[-1] == second[-1]:
            count +=1
        return count + digit_match(first[:-1],second[:-1])
            
    else:
        return count


