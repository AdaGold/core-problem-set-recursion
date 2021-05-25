# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if len(array) == 0:
        return False
    return True if array[-1] == query else False or search(array[:-1], query)

# is_palindrome


def is_palindrome(str):
    if len(str) <= 1:
        return True
    return (True if str[0] == str[-1] else False) and is_palindrome(str[1:-1])


# digit_match
def digit_match(str_1, str_2):
    length = []
    digit_match_internal(str(str_1), str(str_2), length)
    return len(length)


def digit_match_internal(str_1, str_2, len_acc):
    if str_1 == "" or str_2 == "":
        return
    if str_1[-1] == str_2[-1]:
        len_acc.append(1)
    return digit_match_internal(str_1[:-1], str_2[:-1], len_acc)
