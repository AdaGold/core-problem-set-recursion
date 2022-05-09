# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    elif array[0] == query:
        return True
    else:
        return search(array[1::], query)

# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1:-1:])


# digit_match
def digit_match(int1, int2):
    if int1 == 0 and int2 == 0:
        return 1
    elif int1 == 0 or int2 == 0:
        return 0
    elif int1 < 10 and int2 < 10:
        if int1 % 10 == int2 % 10:
            return 1
        else:
            return 0
    elif int1 % 10 == int2 % 10:
        return 1 + digit_match((int1 // 10), (int2//10))
    else:
        return digit_match((int1 // 10), (int2 // 10))
# Emotionally I would rather make the question match "positive integers",
# toss test 4, and write the solution
# def digit_match(int1, int2):
#     if int1 == 0 or int2 == 0:
#         return 0
#     elif int1 % 10 == int2 % 10:
#         return 1 + digit_match((int1 // 10), (int2//10))
#     else:
#         return digit_match((int1 // 10), (int2 // 10))
# which is much prettier... unless part of the question was learning
# "handling edge cases using recursion is annoying"
# which, fair, if so. (wish the hint was about that, though,
# instead of about floor division!)

## I had to solve the problem this way
# def digit_match(int1, int2):
#     int1 = str(int1)
#     int2 = str(int2)
#     if len(int1) == 0 or len(int2) == 0:
#         return 0
#     if int1[-1] == int2[-1]:
#         return 1 + digit_match(int1[:-1], int2[:-1])
#     else:
#         return 0 + digit_match(int1[:-1], int2[:-1])
## and look at the Ada explanation solution
## to figure out how to handle the "match 0 to 0" case
## ._."
