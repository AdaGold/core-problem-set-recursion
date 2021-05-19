# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
     
    if n == 0:
        return 1
    
    if n < 0:
        raise ValueError

    if n == 1:
        return 1
    
    return n * factorial(n - 1)


# reverse
def reverse(text):
    
  if (len(text) == 0):
    return text
    
  if (len(text) == 1):
    return text[0]

  return text[-1] + reverse(text[:-1])


# bunny
def bunny(num_of_bunnies):
    
  if (num_of_bunnies == 0):
    return 0

  if (num_of_bunnies == 1):
    return 2

  return 2 + bunny(num_of_bunnies - 1)


# is_nested_parens
def is_nested_parens(paren_str): 

  length = len(paren_str)

  if length % 2 != 0:
    return False

  if (length == 0):
    return True

  start_paren = paren_str[0]
  end_paren = paren_str[-1]
  is_nested = start_paren == "(" and end_paren == ")"

  substring = paren_str[1:length-1]

  print(f"{is_nested} and is_nested_sol('{substring}')")

  return is_nested and is_nested_parens(substring)

