#887. Super Egg Drop
"""
Time Complexity: O(n*k*logn)
Space Complexity: O(n*k)
"""
class Solution:
    def __init__(self):
        self.t = []
    def superEggDrop(self, k: int, n: int) -> int:
        self.t = [[-1 for _ in range(n+1)] for _ in range(k+1)]        
        return self.solve(k,n)
    def solve(self,k,n):
        if k == 1 or n == 1 or n == 0:
            return n
        if self.t[k][n] != -1:
            return self.t[k][n]
        res = float('inf')
        l = 0
        h = n
        while l <= h:
            m = (l + h) // 2
            left = self.solve(k-1,m-1)
            right = self.solve(k, n-m)
            temp = 1 + max(left,right)
            if left < right:
                l = m+1
            else:
                h = m-1
            res = min(res,temp)
            self.t[k][n] = res
        return res
