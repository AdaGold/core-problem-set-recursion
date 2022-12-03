# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
# def search(array, query):
#     if query in array:
#         return True
#     else: 
#         return False

def search(array, query):
    if len(array) == 0:
        return False
    elif array[0] == query:
        return True
    
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return False

    
    return is_palindrome(text[1:-1])


# digit_match

    # if len(apples) == 0 or len(oranges) == 0:
    #     return count
    # elif apples[-1] == oranges[-1]:
    #     count += 1
    
    # return digit_match(apples[:-1], oranges[:-1])


# def digit_match(apples, oranges):
#     count = 0
#     apples = str(apples)
#     oranges = str(oranges)
    
#     loop_string = ""
#     if len(apples) < len(oranges):
#         loop_string = apples
#     else: 
#         loop_string = oranges
    
#     for i in range(1,len(loop_string)+1):
#         if apples[-i] == oranges[-i]:
#             count += 1
            
#     return count

def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
    elif apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        
        return 0
    
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
        
    return digit_match(apples // 10, oranges // 10)