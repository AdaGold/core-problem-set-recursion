'''Write a function bunny that accepts an integer parameter count. count represents a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

Here are the tests:

def test_bunny_zero_bunnies():
    assert bunny(0) == 0


def test_bunny_one_bunny_has_two_ears():
    assert bunny(1) == 2


def test_bunny_fifty_bunnies_have_100_ears():
    assert bunny(50) == 100'''


def bunny_2(count):
    if count == 0:
        return 0
    return 2+(bunny_2(count-1))

print(bunny_2(5))



#Learn solution
def bunny(count):
    if not count:
        return count
    else:
        return 2 + bunny(count-1)
    
def bunny(count):
    if count == 0 :
        return 0
    else:
        return 2 + bunny((count-1))


# print(bunny(2))

# bunny(1) 1*2 count * 2
# bunny(2) 2*2 (count+1) * 2
# bunny(3) 3*2 (count+2) * 2
# bunny(4) 4*2 (count+3) * 2