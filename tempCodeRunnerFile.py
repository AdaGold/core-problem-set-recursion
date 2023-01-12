def is_nested_parens(parens, i=0, cnt=0):
    if type(parens) != str:
        raise TypeError("TypeError")
    
    # if len(parens) % 2 != 0:
    #     return False

    # if parens == "":
    #     return ""
    
    if i == len(parens): return cnt==0
    if cnt<0:return False
    if parens[i] == "(": return is_nested_parens(parens, i+1, cnt+1)
    elif parens[i] == ")": return is_nested_parens(parens, i+1, cnt-1)
    return is_nested_parens(parens, i+1, cnt)
    # base
    
    #recusion
    # return is_nested_parens()

print(is_nested_parens("(())("))