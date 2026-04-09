class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict={}
        for i in range(0,len(arr)):
            if arr[i] in dict:
                dict[arr[i]]=dict[arr[i]]+1
            else:
                dict[arr[i]]=1
        res=set()
        for key in dict:
            if dict[key] in res:
                return False
            else:
                res.add(dict[key])
        return True
arr=[1,2,2,1,1,3]
print("Is the number of occurrences of each value in the array is unique?",Solution().uniqueOccurrences(arr))