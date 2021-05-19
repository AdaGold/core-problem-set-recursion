# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def bin_search(sorted_array, query):
    
  if (len(sorted_array) == 1):
    return query == sorted_array[0]

  mid_index = int(len(sorted_array)/2)

  half1 = sorted_array[0:(mid_index)]
  half2 = sorted_array[mid_index:len(sorted_array)]

  #print(f"mid_index = {mid_index}, len:{len(sorted_array)}, half1:{half1}, half2:{half2}")

  if (query >= half1[0] and query <= half1[-1]):
    return bin_search(half1, query)
  elif (query >= half2[0] and query <= half2[-1]):
    return bin_search(half2, query)
  else:
    return False


# is_palindrome
def is_palindrome(text):
  length = len(text)

  if (length == 1):
    return True

  start_letter = text[0]
  end_letter = text[-1]
  is_palin = start_letter == end_letter

  subpalin = text[1:length-1]

  print(f"{is_palin} and is_palin_sol {subpalin}")

  return is_palin and is_palindrome(subpalin)


# digit_match
def digit_match(n, m):

  if (n < 0 or m < 0):
    return 0
  
  #if (len(m) == 1 or len(n) == 1):
  #  m[-1] == n[-1]

  str_n = str(n)
  str_m = str(m)

  #print(f"str_m = {str_m}, str_n = {str_n}")

  is_digit_match = str_n[-1] == str_m[-1]

  if (len(str_n) == 1 or len(str_m) == 1):
    return is_digit_match

  int_n = int(str_n[0:-1])
  int_m = int(str_m[0:-1])

  num_matches = 0

  if (is_digit_match):
    num_matches += 1
  
  return num_matches + digit_match(int_n, int_m)

