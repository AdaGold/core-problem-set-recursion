# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not len(array):
        return False
    elif array[0] == query:
        return True
   
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
  
    elif text[:1] != text[-1:]:
        return False
    else:

        return is_palindrome(text[1:-1])


# digit_match
def digit_match(number_one, number_two):
    if len(str(number_one)) == 0 or len(str(number_two)) == 0:
        return 0

    difference = int(number_one) - int(number_two)
    if difference/10 == difference//10:
        return 1 + digit_match(str(number_one)[0:-1], str(number_two)[0:-1])

    else:
        return 0 + digit_match(str(number_one)[0:-1], str(number_two)[0:-1])

