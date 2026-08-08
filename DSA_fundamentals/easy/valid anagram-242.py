#Time complexity=O(n)
#space complexity=O(1)
#think of ascii values
#think of string concatination
##if two string has same values then s-t=0

class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
            return False
        hashmap = {}
        for num in s:
            hashmap[num]=hashmap.get(num,0)+1
        
        for num in t:
            hashmap[num]=hashmap.get(num,0)-1
        for value in hashmap.values():
            if value!=0:
                return False
        return True