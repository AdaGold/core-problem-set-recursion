# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array==[]:
        return False
    
    first_el=array[0]
    rest_elements=array[1:]
    
    if first_el==query:
        return True
    else:
        return search(rest_elements,query)


# is_palindrome
def is_palindrome (text):
    if len(text)<=1:
        return True
        
    first_element=text[0]
    last_element=text[-1]
    
    if first_element != last_element:
        return False
    else:
        subproblem=text[1:-1]
        return is_palindrome (subproblem)


# digit_match

def digit_match(num_1,num_2):
    n_1_first_element=num_1 % 10 # gives the reminder(last digit)
    n_2_first_element=num_2 % 10
    
    match=0
    if n_1_first_element== n_2_first_element:
        match=1
    
    if num_1//10==0 or num_2 //10==0: # // integer division: if any of numbers is single digit(less than 10)
        return match
       
    else:
        new_num_1=num_1//10
        new_num_2=num_2//10
        return match + digit_match(new_num_1,new_num_2)
        
