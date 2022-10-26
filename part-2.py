# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(a_list,chara):
    if len(a_list)==0:
        return False
    if a_list[0]==chara:
        return True
    return search(a_list[1:],chara)

# is_palindrome

def is_palindrome(string):
    if len(string)<2:
        return True
    if string[0]==string[-1]:
        return is_palindrome(string[1:-1])
    return False

# digit_match

def digit_match(a,b):
    if a == 0 and b == 0:
        return 1
    elif a < 10 or b < 10:
        if a % 10 == b % 10:
            return 1
        return 0
    if a%10 == b%10:
        return digit_match(a//10,b//10) + 1
    return digit_match(a//10,b//10)
