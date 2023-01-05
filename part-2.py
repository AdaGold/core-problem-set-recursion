# -------------------------------------------------
# search
def search(array, query):
  if len(array) == 0:
    return False
  elif array[-1] == query:
    return True
  else:
    return search(array[:-1], query)

# -------------------------------------------------
# is_palindrome
def is_palindrome(text):
  if len(text) < 2: 
    return True
  if text[0] != text[-1]:
    return False
  return is_palindrome(text[1:-1])

# -------------------------------------------------
# digit_match
def digit_match(n1, n2):
  if n1 == 0 or n2 == 0:
    return 1 if n1 == n2 else 0

  if n1 != n2 and n1 // 10 != n2 // 10:
    count = 1 if n1 % 10 == n2 % 10 else 0
  else:
    return 0
  return count + digit_match(n1 // 10, n2 // 10)

