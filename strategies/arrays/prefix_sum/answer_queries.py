# [1,3,6,10,15]
# #  i 
# #    j

# i = 1
# j = 3
# nums[j] - nums[i-1]

def answer_queries(nums, queries, limit):
	prefix=[nums[0]]
	res = []
	for i in range(1, len(nums)):
		prefix.append(nums[i] + prefix[len(prefix) - 1])
	for i, j in queries:
		if i == 0:
			res.append(prefix[j] < limit)
		else:
			res.append((prefix[j] - prefix[i-1]) < limit)
	return res

print(answer_queries([1,2,3,4,5],[[0,4]],16))

""" OR """
#  If we want the sum of the subarray from i to j (inclusive), then the answer is prefix[j] - prefix[i - 1], or prefix[j] - prefix[i] + nums[i] if you don't want to deal with the out of bounds case when i = 0.

# Without the prefix sum, answering each query would be O(n)O(n) in the worst case, where nn is the length of nums. If m = queries.length, that would give a time complexity of O(n∗m)O(n∗m). With the prefix sum, it costs O(n)O(n) to build, but then answering each query is O(1)O(1). This gives a much better time complexity of O(n+m)O(n+m). We use O(n)O(n) space to build the prefix sum.

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans