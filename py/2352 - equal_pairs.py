'''
    
    [
        [1,2,3],
        [3,4,5],
        [6,7,8
    ]
'''
'''
 Official

'''
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_key(arr):
            # Python is quite a nice language for coding interviews!
            return tuple(arr)
        
        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1
        
        dic2 = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            
            dic2[convert_to_key(current_col)] += 1

        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]
        
        return ans

'''
    [13,13,13],
    [13,13,13],
    [13,13,13],

    Time O(n^2) -> We visit a total of n^2 elements in an n x x grid
    Space (On^2) -> Worst case -> All elements are unique, we store a key for every single item, 
    when accounting for traversal of horizontal and vertical values
'''

from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = 0
        n = len(grid)
        cols = dict()
        rows = dict()

        for i in range(n):
            row = grid[i]
            row_key = tuple(row)
            rows[row_key] = rows.get(row_key, 0) + 1

            j = 0
            col = []
            while j < n:
                el = grid[j][i]
                col.append(el)
                j += 1 
            col_key = tuple(col)
            cols[col_key] = cols.get(col_key,0) + 1


        for key in rows:
            if key in cols:
                c += cols[key] * rows[key]

        return c








