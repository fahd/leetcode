s = 'aAcC'
set_s = set(s)
s2 = 'bbbbAAAcCCC'
sum_2 = [i in set_s for i in s2]
print('sum_2',sum(sum_2))
