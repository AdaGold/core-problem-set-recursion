# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if len(array) == 0:
        return False
    # for char in array:
    #     if char == query:
    #         return True
    #     else:
    #         return True
    if query == array[-1]:
        return True
    return search( array[:-1], query)



# is_palindrome
def is_palindrome(text):
    if len(text) == 0:
        return True
    
    first_char = text[0]
    # print(first_char)
    last_char = text[-1]
    
    # reverse = remaining_chars + first_char
    if len(text) < 2 or first_char == last_char:
        return is_palindrome(text[1:-1])

    else:
        False
    



# digit_match
def digit_match(nums1, nums2, my_match= 0):
    
    num_list1 = str(nums1)
    num_list2 = str(nums2)
    
    if len(num_list1) == 0 or len(num_list2) == 0:
        print(my_match)
        return my_match
    elif num_list1[-1] == num_list2[-1]:
        return digit_match(num_list1[:-1], num_list2[:-1], my_match + 1)
            
    elif num_list1[-1] != num_list2[-1]:
        return digit_match(num_list1[:-1], num_list2[:-1], my_match)