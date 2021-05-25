# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(list_of_ints, int_to_find, index = 0):
    if len(list_of_ints) == 0 or index >= len(list_of_ints):
        return False
    if list_of_ints[index] == int_to_find:
        return True
    return search(list_of_ints, int_to_find, index + 1)



# is_palindrome
def is_palindrome(text):
    if len(text) < 2:
        return True
    
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
        
    return False



# digit_match
def digit_match(int_1, int_2):
    if int_1 == 0 and int_2 == 0:
        return 1
        
    if int_1 <= 0 or int_2 <= 0:
        return 0
        
    if int_1 % 10 == int_1 or int_2 % 10 == int_2:
        if int_1 % 10 == int_2 % 10:
            return 1
        return 0
    
    if int_1 % 10 == int_2 % 10:
        return 1 + digit_match(int_1 // 10, int_2 // 10)
        
    return 0 + digit_match(int_1 // 10, int_2 // 10)

