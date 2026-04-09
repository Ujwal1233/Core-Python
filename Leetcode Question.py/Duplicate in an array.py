class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict={}
        res=[]
        for i in range(0,len(nums)):
            if nums[i] in dict:
                res.append(nums[i])
            else:
                dict[nums[i]]=1
        return res
nums=[4,3,2,7,8,2,3,1]
print("Duplicate elements in the array are:",Solution().findDuplicates(nums))
