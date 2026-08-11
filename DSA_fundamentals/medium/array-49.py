#Time complexity =O(n*K log K)
#Space complexity = O(n*k) n word k characters

class Solution(object):
    def groupAnagrams(self, strs):
        hashmap={}
        for num in strs:
            key=''.join(sorted(num)) #joins the string into one string
                                    #sorted(num) gives list like['a','e','t'] and key ='aet'
            if key not in hashmap:
                hashmap[key]=[]   

            hashmap[key].append(num)
        return list(hashmap.values())