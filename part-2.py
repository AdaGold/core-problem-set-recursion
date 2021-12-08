# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):

    if len(array) == 0:
        return False

    item = array.pop()

    if item == query:
        return True

    return search(array, query)


# is_palindrome
def is_palindrome(text):

    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


# digit_match
# I did this two ways, once with changing the digits to strings and once with math

# string version
def digit_match(n, m):

    n = str(n)
    m = str(m)

    if len(n) == 0 or len(m) == 0:
        return 0

    if n[-1] == m[-1]:
        score = 1
    else:
        score = 0

    return score + digit_match(n[:-1], m[:-1])

# math version
def digit_match(n, m):

    if n % 10 == m % 10:
        score = 1
    else:
        score = 0

    if n / 10 < 1 or m / 10 < 1:
        return score

    return score + digit_match(n // 10, m // 10)