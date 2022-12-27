# def power(num, exponent):
#     if exponent == 0:
#         return 1

#     return num * power(num, exponent - 1)

# print(power(3,6))

def power(num, exponent):
    print("Calling power! num:", num, "exponent:", exponent)
    if exponent == 0:
        return 1

    return num * power(num, exponent - 1)


print(3, "raised to the power of", 5, "is", power(3, 5))

print("-------------")

print(3, "raised to the power of", 6, "is", power(3, 6))