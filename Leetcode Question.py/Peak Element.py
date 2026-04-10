class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        
        if n == 1:
            return 0
        
        for i in range(n):
            if (i == 0 or arr[i] >= arr[i - 1]) and (i == n - 1 or arr[i] >= arr[i + 1]):
                return i
        
        return -1
# Example usage:
sol = Solution()
print(sol.peakElement([1, 2, 3, 1]))  # Output: 2
    