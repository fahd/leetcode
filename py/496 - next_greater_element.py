class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hm = {}
        a = []

        for i,n in enumerate(nums2):
            while stack and n > nums2[stack[-1]]:
                top_stack = nums2[stack[-1]]
                hm[top_stack] = n
                stack.pop()

            stack.append(i)
            hm[n] = -1
        
        for n in nums1:
            a.append(hm[n])
        
        return a

            
            


        
