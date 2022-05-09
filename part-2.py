# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    if query == array[0]:
        return True
    else:
        return search(array[1:], query)


# is_palindrome
def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    return False


# digit_match
# ** Works for all cases except initial case (0, 0) ***
# ** Any variation I tried caused loss of functionality for other cases **
def digit_match(int_1, int_2):
    count = 0
    if int_1 == 0 or int_2 == 0:
        return count

    if int_1 == 0 and int_2 == 0:
        return 1
    elif int_1 % 10 == int_2 % 10:
        count += 1
        return count + digit_match(int_1//10,int_2//10)
    else:
        return digit_match(int_1//10,int_2//10)

