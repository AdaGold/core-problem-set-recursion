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

    # Is it best practive for a new list to be created?
    array.remove(array[0])

    # return False or search(array, query) -- False not necessary
    # until the last "iteration"
    return search(array, query)


# is_palindrome
# The idea of using a helper function for recursion seemed
# intimidating so I tried it here. Also, I had already created
# a function to reverse text.
def is_palindrome(text):
    return reverse(text) == text


def reverse(text):
    if text == "":
        return ""

    letter = text[len(text) - 1]
    text = text[:-1]

    return letter + reverse(text)

# digit_match
# Saving for extra practice after studying recursion more.
