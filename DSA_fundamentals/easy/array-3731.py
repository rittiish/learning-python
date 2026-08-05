#Time complexity = O(n)
#space complexity = O(1)
#Easy type of daily leetcod streak
class Solution(object):
    def findMissingElements(self, nums):
        minimum=min(nums)
        maximum=max(nums)
        arr=[]
        hashTable=[0]*101
        for i in nums:
            hashTable[i]+=1

        for num in range(minimum + 1,maximum):
            if(hashTable[num]==0):
                arr.append(num)
        return arr

