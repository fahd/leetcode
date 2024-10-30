def sortedSquares(nums):
        n = len(nums)
        l, r = 0, n - 1
        res = [0] * n
        i = n - 1

        while l <= r:
            l_abs = abs(nums[l])
            r_abs = abs(nums[r])

            if l_abs < r_abs:
                res[i] = r_abs ** 2
                r -= 1
            else:
                res[i] = l_abs ** 2
                l += 1
            i -= 1
        return res
    


print('sortedSquared:', sortedSquares([-4,-3,-2,-1,0,1]))