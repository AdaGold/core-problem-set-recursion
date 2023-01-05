# -------------------------------------------------
# factorial
def factorial(n):
  if n == 0:
      return 1
  elif n < 0:
    raise ValueError('ValueError')

  return n * factorial(n-1) 

# -------------------------------------------------
# reverse
def reverse(text):
  if len(text) == 0:
    return text
  else:
    return reverse(text[1:]) + text[0]

# -------------------------------------------------
# bunny
def bunny(count):
  if count == 1:
    return 2
  elif count == 0:
    return 0
  else:
    return 2 + bunny(count-1)

# -------------------------------------------------
# is_nested_parens
def is_nested_parens(parens):
  if len(parens) < 2:
    return True
  if parens[0] == parens[-1] or len(parens)%2 != 0:
    return False
  return is_nested_parens(parens[1:-1])

