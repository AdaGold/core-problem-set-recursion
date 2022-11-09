# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array , query):
    #base case
    if not array:
        return False
    #recursive case 
    elif query == array[-1]:
        return True
    return search(array[:-1], query)


# is_palindrome



# digit_match


