#Time complexity =O(n)
#space complexity=O(1)
#topic = moore's voting algorithm

class Solution(object):
    def majorityElement(self, nums):
        
        count=0
        element=None
        for num in nums:
            if count ==0:
                element =num
            if num==element:
                count+=1
            else:
                count-=1
        return element