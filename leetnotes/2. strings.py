''' =========== STRINGS =========== '''

# strings are immutable. building a new string requires copying, which is o(n) every time

# a = ["a","b","c"] ====> have to be strings
# st = ",".join(a)
# print('st:', st) =====> a,b,c

''' Looping '''
s = 'test'
for c in s:
	print('c:',c)

''' Looping over object '''
dic = {	'a': 1, 'b': 2, 'c': 3}
for key in dic.keys():
	# print('key',dic[key])

for key,value in dic.items():
	# print('key', key)
	# print('value', value)



''' Convert array into string '''
l1 = [1,2,3]
print('str:', str(l1))



''' -- '''



''' Check if string is alphabetic'''
str.isalpha()



''' Ord '''
# The ord() function in Python returns the Unicode code point of a given character. 
# Essentially, it converts a character (a single letter or symbol) into an integer that represents its position in the Unicode character set.
