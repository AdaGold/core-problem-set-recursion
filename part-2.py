# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    i = 0
    # base case
    if i >= len(array):
        return False
    elif array[i] == query:
        return True
    else:
        return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    # base cases
    if len(text) == 0:
        return True
    elif text[0] != text[-1]:
        return False
    else:
        # recursive case
        return is_palindrome(text[1:-1])



# digit_match
def digit_match(x, y):
    """
    :params:
    - x, y (int): two numbers to compare digits
    :returns:
    - matches (int): number of matched digits between numbers
    """
    # ~~~ base cases ~~~
    # check if x and y are 0
    if x == 0 and y == 0:
        return 1
    # check if x and y are less than 10
    elif x < 10 or y < 10:
        # check if ones place digits match
        if x % 10 == y % 10:
            return 1
        else:
            # no match == 0
            return 0
    else:
        # recursive case
        if x % 10 == y % 10:
            return 1 + digit_match(x//10, y //10)
        else: 
            return digit_match(x//10, y//10)

