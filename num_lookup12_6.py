# arr = [5, 8, 1, 3, 7, 5, 6]
# num = 3

# def num_look_up(arr, num):
# 	arr.sort()
	
# 	if num > len(arr):
# 		return None
# 	else:
# 		num = arr[-num]

'''
Given an array, a start position, and an end position, remove the values within that start-end range "in-place," then return the original array. Don't use slice. Don't forget edge cases!

Example Input: [5, 8, 1, 3, 7, 5, 6,10], 3, 6
Example Output: [5, 8, 1, 10]

Example Input: [4, 5, 6, 7, 10, 11, 12, 13], 5,7
Example Output: [4, 5, 6, 7, 10]

Example Input: [4, 5, 6, 7, 10, 11, 12, 13], 7,11
Example Output: [4, 5, 6, 7, 10, 11, 12]

'''
arr = [4, 5, 6, 7, 10, 11, 12, 13]
start = 5
end=7

def remove_nums_in_range(arr,start,end):
    for idx in range(end,start-1,-1):
        arr.pop(idx)
    return arr

print(remove_nums_in_range(arr,start,end))