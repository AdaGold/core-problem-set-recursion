# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    # establish base case: 0 or 1
    if n <= 1 and n >= 0:
        return 1
    elif n < 0:
        raise ValueError("number must be postiive")
        
    # establish Recursive case: find factorial of n-1 and multiply it by n
    else:
        return n * factorial(n-1)



# reverse
def reverse(text):

    # Base case: a string of length 0 or 1
    if len(text) <= 1:
        return text

    else:
        # Recursive case: concatenate the last char of str
        last_char = text[-1]
        substring = text[1:-1]
        # w/ reverse of substring from  second char to the second-to-last char
        return last_char + reverse(substring) + text[0]

# bunny
def bunny(count):
    # Base case: 0 bunny means no ears
    if count == 0:
        return 0

    # Recursive case: 2 ears per bunny plus count of ears on other bunnies
    else:
        return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    # Base case: empty str means proper nesting
    if not parens:
        return True

    # Base case: odd len str is improper nesting
    if len(parens) % 2 != 0:
        return False

    # Recursive case: if the first and last chara are matching parens, check substring btwn chars
    else:
        if parens[0] == "(" and parens[-1] == ")":
            return is_nested_parens(parens[1:-1])
        else:
            return False

