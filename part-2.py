# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(list, number): 
    if len(list) == 0: 
        return False 
    elif list[0] == number: 
        return True 
    return search(list[1:], number)

# is_palindrome
def reverse(text):
    if len(text) <= 1: 
        return text
    return reverse(text[1:]) + text[0]

def is_palindrome(text): 
    if reverse(text) == text: 
        return True
    return False

# digit_match
def digit_match(num_1, num_2): 
    str_1 = str(num_1)
    str_2 = str(num_2)
    count = 0 

    if len(str_1) == 0 or len(str_2) == 0: 
        return count 
    elif str_1[-1] == str_2[-1]: 
        count += 1 
    return count + digit_match(str_1[:-1], str_2[:-1])

