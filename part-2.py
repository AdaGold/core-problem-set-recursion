# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(arr, query):
    if not arr:
        return False
    elif query == arr[-1]:
        return True
    else:
        arr.pop()
        return search(arr, query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[:1] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
    else:
        count = 0
        last_digit_apples = apples % 10
        last_digit_oranges = oranges % 10
        if last_digit_apples == last_digit_oranges:
            count += 1
        if apples // 10 == 0 or oranges // 10 == 0:
            return count
        else:
            return count + digit_match(apples//10, oranges//10)

