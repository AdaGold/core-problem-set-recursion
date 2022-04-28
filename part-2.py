# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):

    if not all([array, query]):
        return False

    if array[-1] == query:
        return True
    else:
        array.pop()
        return search(array, query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif not text[0].isalnum():
        return is_palindrome(text[1:])
    elif not text[-1].isalnum():
        return is_palindrome(text[:-1])
    elif text[0].lower() == text[-1].lower() and is_palindrome(text[1:-1]):
        return True
    else:
        return False

# is_palindrome extra challenge


def palindrome_helper(str, left, right):
    if left >= right:
        return True
    elif not str[left].isalnum():
        return palindrome_helper(str, left+1, right)
    elif not str[right].isalnum():
        return palindrome_helper(str, left, right-1)
    elif str[left].lower() == str[right].lower():
        return palindrome_helper(str, left+1, right-1)
    else:
        return False


def is_palindrome2(text):
    return palindrome_helper(text, 0, len(text)-1)

# digit_match


def digit_match(int1, int2):
    if int1 == 0 and int2 == 0:
        return 1

    else:
        count = 0
        if int1 % 10 == int2 % 10:
            count += 1
        if int1//10 > 0 and int2//10 > 0:
            count += digit_match(int1//10, int2//10)
    return count
