# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if len(array) == 0:
        return False
    elif array[0] == query:
        return True
    return search(array[1:],query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])



# digit_match (by converting to string)
def digit_match(input1,input2):
    if type(input1) == int and type(input2) == int:
        input1, input2 = str(input1), str(input2)
    if len(input1) == 1 or len(input2) == 1:
        return 1 if input1[-1] == input2[-1] else 0
    cur_score = 1 if input1[-1] == input2[-1] else 0
    return digit_match(input1[:-1],input2[:-1]) + cur_score


# digit_match (by using mathematical operators)
def digit_match(input1,input2):
    if input1 < 10 or input2 < 10:
        return 1 if input1 % 10 == input2 % 10 else 0
    cur_score = 1 if input1 % 10 == input2 % 10 else 0
    return digit_match(input1 // 10, input2 // 10) + cur_score

