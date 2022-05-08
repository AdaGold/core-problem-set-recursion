# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    last_el = array.pop()
    if last_el == query:
        return True
    return search(array, query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    first = text[0]
    last = text[-1]
    if first != last:
        return False
    new_text = text[1:-1]
    return is_palindrome(new_text)


# digit_match
def digit_match(apples, oranges):
    digit_from_apple = apples % 10
    digit_from_oranges = oranges % 10
    
    count = 0
    if digit_from_apple == digit_from_oranges:
        count += 1
    if apples < 10 or oranges < 10:
        return count
    return count + digit_match(apples // 10, oranges // 10)
    

