# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array)==0:
        return False
    elif array[-1]==query:
        return True
    else:
        return search(array[:-1],query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1 or len(text) == 0:
        return True
    elif text[0]==text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False 


# digit_match
def digit_match(apples,oranges):
    apples_list=[a for a in str(apples)]# Gives a list of ints
    oranges_list=[o for o in str(oranges)]# Gives a list of ints
    
    #This section trims the list to be the same size
    new_apples_list, new_oranges_list=trim_list(apples_list, oranges_list)
    
    # If list is complete 
    if len(new_apples_list)==1:
        return 0 if new_apples_list[0] != new_oranges_list[0] else 1
    
    new_apples=int("".join(new_apples_list[:-1]))
    new_oranges=int("".join(new_oranges_list[:-1]))
    num=1 if new_apples_list[-1] == new_oranges_list[-1] else 0
    return num+int(digit_match(new_apples,new_oranges)) 

def trim_list(apples_list, oranges_list):
    if len(apples_list)!= len(oranges_list):
        if len(apples_list)>len(oranges_list):
            new_apples_list=apples_list[-len(oranges_list):]
            new_oranges_list=oranges_list
        else:
            new_oranges_list=oranges_list[-len(apples_list):]
            new_apples_list=apples_list
    else:
        new_apples_list=apples_list
        new_oranges_list=oranges_list
    return new_apples_list, new_oranges_list

