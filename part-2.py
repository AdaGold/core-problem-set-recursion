# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, letter):
    if len(array) == 0:
        return False
    
    if array[0] == letter:
        return True
    elif array[0] != letter:
        return search(array[1:], letter)


# is_palindrome
def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    return False


# digit_match
def digit_match(a, b):
   
    if a == 0 and b == 0:
        return 1
    if a <10 or b< 10:
        if a%10 == b%10:
            return 1
        else:
            return 0
        
    last_digit_a = a % 10
    last_digit_b = b % 10
    
    remaining_a = a // 10
    remaining_b = b // 10
    
    if last_digit_a == last_digit_b:
        return 1 + digit_match(remaining_a, remaining_b)
    return digit_match(remaining_a, remaining_b)

