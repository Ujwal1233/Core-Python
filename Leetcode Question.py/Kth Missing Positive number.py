class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        current_number = 1
        index = 0
        
        while missing_count < k:
            if index < len(arr) and arr[index] == current_number:
                index += 1
            else:
                missing_count += 1
            
            if missing_count == k:
                return current_number
            
            current_number += 1
        
        return current_number
# Example usage:
sol = Solution()
print(sol.findKthPositive([2, 3, 4, 7, 11], 5))  # Output: 9  
