# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(arr, query):
    if not arr:
        return False

    if arr[0] == query:
        return True

    return search(arr[1:], query)


# is_palindrome
def is_palindrome(text):
    if not isinstance(text, str):
        return False

    if len(text) <= 1 or text.isspace():
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    # Extract the last digits of both numbers
    digit1 = num1 % 10
    digit2 = num2 % 10

    # Recursively test the remaining digits
    remaining_match = 0
    if (num1 // 10) != 0 and (num2 // 10) != 0:
        remaining_match = digit_match(num1 // 10, num2 // 10)

    if digit1 == digit2:
        remaining_match = remaining_match + 1

    return remaining_match

