#Time complexity=O(n)
#Space complexity=O(1)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        maximum=0
        lenght=0
        hashmap={}
        for right in range(len(s)):
            if s[right] not in hashmap:
                hashmap[s[right]]=right
            else:
                left=max(left,hashmap[s[right]]+1)
                hashmap[s[right]]=right
            length=(right-left)+1
            maximum=max(length,maximum)
        return maximum

    