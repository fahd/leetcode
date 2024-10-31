''' =========== OBJECTS ==========='''
o = {'a':1,'b':2, 'c':3}

# for item in o:
#     print('item',item)

# for (key, value) in o.items():
#     print('key',key, 'value', value)

# for key in o.keys():
#     print('key',key)

''' Check if exists in dict '''
print('a' in o) # True
print('1' in o) # False



''' Delete in dict '''
del o['a']
print('o',o)



''' Length of dict '''
print(len(o)) # 2


''' Values of dict '''
values = o.values()
for val in values:
	print('val',val)