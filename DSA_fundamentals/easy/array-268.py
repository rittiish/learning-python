#Time complexity=O(n)
#space complexity=O(1)

class Solution(object):
    def missingNumber(self, nums):
        hashList=[0]*(len(nums)+1)

        for num in nums:
            hashList[num]+=1
        for num in range(len(hashList)):
            if(hashList[num]==0):
                return num
