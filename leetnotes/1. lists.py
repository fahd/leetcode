''' =========== LISTS =========== '''
arr1 = [1,2,3]

''' Looping in a list'''
#  for item in arr:
#     print('item',item)

# for i in range(0,len(arr)):
#     print('i',i)
#     print('value',arr[i])
# SAME AS
# for i in range(len(arr)):
#     print('i',i) # starts from 0

''' Enumeration '''
for i,val in enumerate([1,2,3]):
	print('i',i)
	print('val',val)



''' Adding items in array '''
l = sum([1,2,3,4,5])



''' Creating a list from characters '''
list_of_chars = list('abc')
# ['a','b','c']



''' Deconstructing an array of arrays '''
arr2  = [[0,1], [2,3], [4,5]]
# for a, b in arr2:
# 	print('a',a,'b',b) # a:0, b: 1



''' Deconstructing an array of variable length '''
arr3 = [[0, 1, 2], [1, 2]]
# for a, *rest in arr3:
#     print(f"a = {a}, rest = {rest}")



''' Filling in an array with predetermined values ''' 
n = 15
arr4 = [0] * n



''' Going backwards '''
# for i in range(len(l) - 1, -1, -1):


''' List comprehension '''
l1_sorted = [0,4,9,12,34]
l1_sorted = [x ** 2 for x in l1_sorted]
# print('l1_sorted:', l1_sorted)



''' Sorting '''###
arr5 = [4,1,3,2]
# print(arr5.sort()) # modify in place
# print(sorted(arr5)) # creates a new list


''' =========== TUPLES =========== '''
# Tuples are immutable
arr6 = [1,2,3,4,5]
# arr_to_tuple = tuple(arr)
# print('arr_to_tuple:', arr_to_tuple)
