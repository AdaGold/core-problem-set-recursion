# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array_letters, letter):

    if array_letters == []:
        return False
    else:
        if array_letters[0] != letter:
            chunk_array = array_letters[1:len(array_letters)]
            return search(chunk_array, letter)
        else:
            return True


# is_palindrome
def is_palindrome(text):
    
    if len(text) == 1 or text == "":
        return True
    
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match
def digit_match(apples, oranges):
    if apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        else:
            return 0
            
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
    else:
        return digit_match(apples // 10, oranges // 10)

