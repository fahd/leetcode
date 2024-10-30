def running_sum(nums):
	prefix_sum=[nums[0]]
	for i in range(1,len(nums)):
		prefix_sum.append(nums[i] + prefix_sum[-1])
	return prefix_sum