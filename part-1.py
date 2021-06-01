# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    
    
    if num == 0:#base case
        return 1
    return num * factorial(num-1)
    # (4)
      #4 * (4-1)
        #3 * (3-1)
         #2 * (2-1)
          #1 

# reverse
def reverse(text):
    if text =="":
        return text
    return text[-1] + reverse(text[:-1])# [:-1] makes is shorter
#  "lacy"   
#     "y" + reverse("lac")
#      "y" + "c" + reverse("la")
#       "y" + "c" + "a" + reverse("l")
#         "y" +"c" + "a" + "l"  + reverse("")
#           y + c + a + l


# bunny
def bunny(count):
    
    if count == 0:
        return 0
    return  2  + bunny(count - 1)
    
    #bunny(1)= 2 +bunny(0)= 0 


# is_nested_parens

def is_nested_parens(parens):
    
    if parens == "": #base case
        return True
    if parens[0] =='(' and parens[-1] == ')':
        return True and is_nested_parens(parens[1:-1])
    return False
    #result = parens[0] == parens[-1]#result holds a boolean value
   
