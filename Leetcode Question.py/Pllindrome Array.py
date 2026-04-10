
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        n = len(arr)
        
        for i in range(n):
            if arr[i] != arr[n - 1 - i]:
                return False
        
        return True
# Example usage:
sol = Solution()
print(sol.isPerfect([1, 2, 3, 2, 1]))  # Output: True