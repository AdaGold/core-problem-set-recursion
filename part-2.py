# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    if  array[0] != query:
        return search(array[1:], query)
    return True 

# print (search(["a", "b", "c"], "a"))


# is_palindrome
def is_palindrome(text):
    text = text.lower()
    #return true or false 
    #assume upper and lower case matter
    if (len(text) <=1 ):
        return True 
    if text[0] == text[len(text) -1]:
        return is_palindrome(text[1: len(text)- 1])

    return False 


# digit_match
def digit_match(first_num, second_num):
    if first_num == 0 and second_num == 0:
        return 1
    
    elif first_num < 10 or second_num < 10:
        if first_num % 10 == second_num % 10:
            return 1
        return 0

    if first_num % 10 == second_num % 10:
        return 1 + digit_match(first_num // 10, second_num // 10)
    return digit_match(first_num // 10, second_num // 10)


# print (digit_match(12354, 12543))

