# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array:str, query:str) -> bool:
    if not array:
        return False
    elif array[0] == query:
        return True
    
    return search(array[1::], query)


# is_palindrome
def is_palindrome(text:str) -> bool:
    if text == "" or len(text) == 1: 
        return True
    
    return text[0] == text[-1] and is_palindrome(text[1:-1])


# digit_match
# this one was really difficult for me & it looks so ugly, lol
def digit_match(num_a:int, num_b:int) -> int:
    if num_a == 0 and num_b == 0:
        return 0
    elif num_a < 10 or num_b < 10: 
        if num_a == num_b:
            return 1
        elif num_a % 10 == num_b % 10:
            return 1
        else:
            return 0

    if num_a % 10 == num_b % 10: 
        return digit_match(num_a // 10, num_b // 10) + 1 
    else:
        return digit_match(num_a // 10, num_b // 10)

