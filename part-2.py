# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(item_list, item):
    if not item_list:
        return False

    cur = item_list.pop()
    if cur == item:
        return True

    return search(item_list, item)


# is_palindrome (to solve without creating new strings, we could do something like
# what was done in part1 is_nested_parens)
def is_palindrome(text):
    if not text:
        return True
    
    elif text[0] != text[-1]:
        return False
    
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    if num1 < 10 or num2 < 10:
        if num1 % 10 == num2 % 10:
            return 1
        return 0
    elif num1 % 10 == num2 % 10:
        return 1 + digit_match(num1//10, num2//10)
    return digit_match(num1//10, num2//10)

