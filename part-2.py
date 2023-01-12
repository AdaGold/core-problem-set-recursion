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
    else:
        return search(array[1:], query)


# is_palindrome
def is_palindrome(test):
    if len(test) <= 1:
        return True
    if test[0] != test[-1]:
        return False
    else:
        return is_palindrome(test[1:-1])


# digit_match
def helper(num1, num2, counter):
    if num1 == 0 or num2 == 0:
        return counter
    if num1 % 10 == num2 % 10:
        counter += 1
    return helper(num1//10, num2//10, counter)

def digit_match(num1, num2):
    counter = 0
    if num1 == 0 and num2 == 0:
        return 1
    return helper(num1, num2, counter)

