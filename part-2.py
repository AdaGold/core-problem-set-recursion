# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.


# search
def search(array, query):
    
    if array == []:
        return False
        
    else:
        if array[0] == query:
            return True
        return search(array[1:], query)
        

# is_palindrome
def is_palindrome(text, left_index = 0):
    right_index = len(text) - 1 - left_index
    
    if not text or left_index >= right_index:
        return True
    
    elif text[left_index] == text[right_index]:
        return is_palindrome(text, left_index + 1)
    
    return False


# digit_match
def digit_match(num_1, num_2, counter = 0):
    
    if num_1 ==0 and num_2 == 0:
        return True
        
    elif num_1 == 0 or num_2 == 0:
        return counter

    if num_1 % 10 == num_2 % 10:
        counter += 1
        return digit_match(num_1 // 10, num_2 // 10, counter)
    else:
        return digit_match(num_1 // 10, num_2 // 10, counter)
        

