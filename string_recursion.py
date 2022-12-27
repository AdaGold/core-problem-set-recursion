# Problem:
# write a function count_chars(data, char) that counts the 
# occurences of a particular character in a nested list 
# data structure
# example input: ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'a', 'b', 'b', 'd', 'a', 'c'], 'a'
# output: 5

# example input 2: ['a', ['b', 'c', 'd'], ['e', 'a', ['a', ['a']]], ['b', 'b', 'd'], 'a', 'c']
# output: 5

def count_chars(data, char):
    count = 0
    if not data:
        return 0
    
    if isinstance(data[0], str):        
        if data[0] == char:
            count += 1
    
    elif isinstance(data[0], list):
        count += count_chars(data[0], char)
        
    return count + count_chars(data[1:], char)

print(count_chars(['a', 'b', 'c', 'd', 'e', 'a', 'a', 'a', 'b', 'b', 'd', 'a', 'c'], 'a'))


#second solution - not yet working
def count_chars2(data,char):
    count = 0
    for item in data:
         if isinstance(item,list):
            count += count_chars2(item, char)
             
            if item == char:
                count +=1
    return count

print(count_chars2(['a', 'b', 'c', 'd', 'e', 'a', 'a', 'a', 'b', 'b', 'd', 'a', 'c'], 'a'))