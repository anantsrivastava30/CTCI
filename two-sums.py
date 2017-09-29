class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
    
        for i in range(len(nums)):
            d[nums[i]] = i
        
        print(d)
        
        for j in range(len(nums)):
            container = nums[j]
            if target - container in d.keys() and j != d[target - container]:
                return j, d[target - container]