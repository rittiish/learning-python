#Time complexity = O(n+n)=O(n)
#space complexity = O(1)
#Handle the zero cases in array was major part

class Solution(object):
    def productExceptSelf(self, nums):

        value = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                value *= num

        array = []

        for num in nums:
            if zero_count > 1:
                array.append(0)

            elif zero_count == 1:
                if num == 0:
                    array.append(value)
                else:
                    array.append(0)

            else:
                array.append(value // num)

        return array
