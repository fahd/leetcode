class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        l = 0
        r = n - 1
        a = list(s)

        while l < r:
            l_char = a[l]
            r_char = a[r]
            if l_char.isalpha() and r_char.isalpha():
                a[l], a[r] = a[r], a[l]
                l+=1
                r-=1
            elif not l_char.isalpha():
                l += 1
            else:
                r -= 1
        
        return "".join(a)
