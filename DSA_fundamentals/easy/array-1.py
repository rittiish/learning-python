#Time complexity O(n)
#Space complexity O(n)

class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for i,num in enumerate(nums):
            needed=target-num
            if needed in hashmap:   #keys can be stored with values which could be anything,
                                    #its faster to look into a dictionary than list
                return(hashmap[needed],i)
            hashmap[num]=i