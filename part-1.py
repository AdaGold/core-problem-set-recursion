# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
  
    if n < 0:
      raise ValueError

    if n == 0:
      return 1

    return n * factorial(n - 1)


# reverse
# referred to some resources online
def reverse(text):
    
    if not text:
        return text

    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    
    if count == 0:
        return 0
        
    return bunny(count - 1) + 2

# is_nested_parens
# attended recursion review and had an idea of where to start
def is_nested_parens(parens):

  if not parens:
    return True

  if parens[0] == "(" and parens[-1] == ")":
    return is_nested_parens(parens[1:-1])
  else:
    return False

