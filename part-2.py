# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(arr, query):
    if not arr:
        return False
    if query == arr[0]:
        return True
    else:
        return search(arr[1:], query)



# is_palindrome
def is_palindrome(text):
    if not text:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:len(text)-1])


# digit_match
def digit_match(num1, num2):
    if num1 < 9 or num2 < 9:
        if (num1 % 10) == (num2 % 10):
            return 1
        else:
            return 0
            
    return ((num1 % 10) == (num2 % 10)) + digit_match(num1//10, num2//10)

