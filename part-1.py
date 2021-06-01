# Part 1


# factorial❗
def factorial(num):
    if num < 0:
        raise ValueError

    if num == 0:
        return 1

    return num * factorial(num -1)

# 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

# reverse 🔄
def reverse(text):
    if len(text) == 0:
        return ""

    return text[-1] + reverse(text[:-1])

# 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

# bunny 🐰
def bunny(count):
    if count <= 0:
        return 0

    return 2 + bunny(count -1)

# 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

# is_nested_parens? 🤰
def nested_helper(parens, counter=0):  # 🦄 helper
    # update to make it more readable

    if len(parens) == 0:
        return True if counter == 0 else False

    if parens[0] == "(":
        counter += 1
    else:
        counter -= 1

    if counter < 0:
        return False

    return nested_helper(parens[1:], counter)


# 🤰
def is_nested_parens(parens): 
    return nested_helper(parens, 0)

print(is_nested_parens("()(()()((()()))()())()"))

