# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if query not in array:
        return False
    else:
        return True 


# is_palindrome
def is_palindrome(text):
    return text == text[::-1]



# digit_match
def digit_match(apples, oranges):
    count = digit_match_helper(apples, oranges, 0)
    print(count)
    return count
    
    
def digit_match_helper(apples, oranges, counter):
    digit_1 = apples % 10
    digit_2 = oranges % 10
    new_apples = apples // 10
    new_oranges = oranges // 10
    # print(digit_1, digit_2, new_apples, new_oranges)
    
    if digit_1 == digit_2:
        counter += 1
        # Base case
    if new_apples == 0 or new_oranges == 0:
        print(counter)
        return counter
    else: 
        return digit_match_helper(new_apples, new_oranges, counter)
    
    
    

