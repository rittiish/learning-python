#greedy algorithm 
#Time complexity=O(n)
#space complexity=O(1)
class Solution(object):
    def canJump(self, nums):
        maxJump=0
        for i in range(len(nums)):
            if(i>maxJump):
                return False
            maxJump=max(i+nums[i],maxJump)
            
        return True

