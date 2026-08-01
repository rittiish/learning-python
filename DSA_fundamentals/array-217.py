#timeComplexity=O(nlogn)
#space complexity=O(1)
class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        if (len(nums)==1):
            return False
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True
        return False
    
arr =[22,45,6,77,88,22,89,88]
obj = Solution()
print (obj.containsDuplicate(arr))