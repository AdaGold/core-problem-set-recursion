
# factorial
def factorial(n):
        if n == 1:
            return 1
        elif n == 0:
            return 1
        elif n < 0:
            raise ValueError("ValueError")
            return 0
        else:
            return n * factorial(n - 1)


# reverse
def reverse(text):
    if text == "":
        return text
    else:
        return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if not count:
        return count
    else:
        return 2 + bunny(count-1)



# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
      return True
    if len(parens) == 1:
      return False
    if len(parens) == 2:
      return parens[0] + parens[-1] == "()"
    return is_nested_parens(parens[1:-1:])


