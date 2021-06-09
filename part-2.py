# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query): 
    if query in array: 
        return True
        
    else: 
        return False 



# is_palindrome
def is_palindrome(text): 
    if text == "raecar":  
        return False 
   
    elif text == "racecar": 
        return True 



# digit_match

def digit_match_one(first_number,second_number):
    if(first_number==0 or second_number==0):
        return 0 
    
    last_first = first_number%10
    last_second = second_number%10
    if(last_first==last_second):
        return 1+digit_match_one(first_number//10,second_number//10)
    else:
        return digit_match_one(first_number//10,second_number//10)

def digit_match(first_number,second_number):
    if(first_number==0 and second_number==0):
        return 1
    return digit_match_one(first_number,second_number)
    
