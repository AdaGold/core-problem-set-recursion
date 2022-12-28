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

def is_palindrome(s):
# Return True if word is a palindrome, False if not
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])

# digit_match
def digit_match(first_num, sec_num):
    if first_num == 0 and sec_num == 0:
        return 1
    elif first_num < 10 or sec_num < 10:
        if first_num % 10 == sec_num% 10:
            return 1
        
        return 0
        
    if first_num % 10 == sec_num % 10:
        return 1 + digit_match(first_num // 10, sec_num // 10)
        
    return digit_match(first_num// 10, sec_num // 10)

