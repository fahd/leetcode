'''
    [13,13,13],
    [13,13,13],
    [13,13,13],
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








