# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query, i = 0):

    if (i == len(array)):
        return False

    if array[i] == query:
        return True
    
    elif array[i] != query:
        return search(array, query, i + 1)




# is_palindrome

def is_palindrome(text):
    if len(text) < 1:
        return True
    
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match

def digit_match(num1, num2, counter = 0):
    string1 = str(num1)
    string2 = str(num2)
    
    if string1 == "" or string2 == "":
        return counter

    if string1[-1] == string2[-1]:
        counter += 1
        
        return digit_match(string1[:-1], string2[:-1], counter)
    
    else:
        return digit_match(string1[:-1], string2[:-1], counter)
