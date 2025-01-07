# mergesort
class Solution:
    def merge(self,left,right):
        o = []
        il = 0
        ir = 0


        while il < len(left) and ir < len(right):
            if left[il] <= right[ir]:
                o.append(left[il])
                il += 1
            else:
                o.append(right[ir])
                ir += 1
        
        
        while il < len(left):
            o.append(left[il])
            il += 1
        while ir < len(right):
            o.append(right[ir])
            ir += 1

        return o


    def sortArray(self, nums: List[int]) -> List[int]:
        # print(self.merge([1,4],[2,3]))
        if len(nums) < 2:
            return nums
        m = len(nums) // 2
        l = nums[0:m]
        r = nums[m::]
        
        return self.merge(self.sortArray(l), self.sortArray(r))
