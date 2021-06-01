# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(list,letter,left_index=0):
    
    
    if len(list) == 0:
        
        return False
    
    if list[left_index] == letter:
        
        return True
    
    
    
    else:
        
        return  search(list[1:],letter)



# is_palindrome
def is_palindrome(string,left_index=0):
    
    right_index= len(string) -1-left_index
    
    if len(string) == 0:
        return False
        
    if left_index >= right_index:
        return True
    
    if string[left_index] == string[right_index]:
        return is_palindrome(string,left_index+1)
    
    else:
        return False
        


# digit_match
def digit_match(apples,oranges, matches = 0):

    if apples ==0 and oranges == 0:
        return True

    elif apples == 0 or oranges == 0:
        return matches

    if apples % 10 == oranges % 10: #gives back remainder when dividing by 10
        matches += 1 #if remainders are the same, 
        #they both end in 0's and have 1 more match
        return digit_match(apples // 10, oranges // 10, matches)
        #returns floor quotient for both apples and oranges
        #exclusing remainder
        
    else: #if remainders are not the same, then dont add any matches
        return digit_match(apples// 10,oranges// 10, matches)


