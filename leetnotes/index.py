# - The time complexity of an algorithm is the amount of time the algorithm needs to run relative to the input size. 

# - The space complexity of an algorithm is the amount of memory allocated by the algorithm when run relative to the input size.


''' =========== ARRAYS =========== '''
arr = [1,2,3]

#  for item in arr:
#     print('item',item)

# for i in range(0,len(arr)):
#     print('i',i)
#     print('value',arr[i])

# for i in range(len(arr)):
#     print('i',i) # starts from 0

arr2 = [
	[0,1],
	[1,2],
	[2,3]
]

''' Adding items in array '''
l = sum([1,2,3,4,5])

''' Creating a list from characters '''
list_of_chars = list('abc')
# ['a','b','c']

''' Deconstructing an array of arrays '''
# for a, b in arr2:
# 	print('a',a,'b',b)

''' Deconstructing an array of variable length '''
arr3 = [[0, 1, 2], [1, 2]]
# for a, *rest in arr3:
#     print(f"a = {a}, rest = {rest}")

''' Filling in an array with predetermined values ''' 
# arr = [0] * n

''' Going backwards '''
# for i in range(len(l) - 1, -1, -1):



l1_sorted = [0,4,9,12,34]
l1_sorted = [x ** 2 for x in l1_sorted]
# print('l1_sorted:', l1_sorted)

''' ======> sorting '''###
arr = [4,1,3,2]
# print(arr.sort()) # modify in place
# print(sorted(arr)) # creates a new list








''' =========== STRINGS =========== '''

# strings are immutable. building a new string requires copying, which is o(n) every time

# a = ["a","b","c"] ====> have to be strings
# st = ",".join(a)
# print('st:', st) =====> a,b,c











''' =========== OBJECTS ==========='''
o = {'a':1,'b':2, 'c':3}

# for item in o:
#     print('item',item)

# for (key, value) in o.items():
#     print('key',key, 'value', value)

# for key in o.keys():
#     print('key',key)





''' =========== STRINGS ==========='''
# They are immutable




''' 4. =========== MATH ==========='''
n = abs(-1)
print('n:', n)
