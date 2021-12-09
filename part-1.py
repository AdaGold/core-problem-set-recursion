# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 1 or n==0:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[0]

# print(reverse("cat"))
# output: "tac"

# bunny

def bunny(count):
    if count == 0:
        return 0
    elif count == 1:
        return 2
    else:
        return 2 + bunny(count-1)

# print(bunny(50))
# output: 100

# is_nested_parens
def is_nested_parens(parens):

    if parens == "":
        return True

    # Base Case    
    if parens[0] == parens[-1]:
        return False
    else:
        parens[0] == "(" and parens[-1] == ")"
        parens = parens[1:-1]
        return is_nested_parens(parens)

parens = "((()))"
print(is_nested_parens(parens))
# output: True

parens2 = ""
print(is_nested_parens(parens2))
# output: True

no_match = "(())))"
print(is_nested_parens(no_match))
# output: False