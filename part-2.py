# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    # base case
    if not array: 
        return False
    if array.pop() == query:
        return True

    return search(array[:-1], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1]) 
    else:
        return False


# digit_match
def digit_match(num1, num2):
    #base case
    if num1 == num2:
        return 1

    if (num1 % 10) == (num2 % 10):
        #base case
        if num1 < 10 or num2 < 10:
            return 1
        return 1 + digit_match((num1)//10, (num2)//10)

    elif num1 >= 10 and num2 >= 10:
        return digit_match((num1)//10, (num2)//10)
    return 0

