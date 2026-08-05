#Time complexity = O(m+n)
#Space complexity = O(1)

class Solution(object):
    def intersection(self, nums1, nums2):
        hash_list={}
        array=[]
        for num in nums1:
            if num in hash_list:
                hash_list[num]+=1
            else:
                hash_list[num]=1

        for num in nums2:
            if num in hash_list:
                array.append(num) 
                del hash_list[num] # used to keep only uniqe intersection elements in array,
                                   # every time key is added in array its deleted form  hash_list
        return array


            