class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        max_l = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                l = l + 1
            else:
                max_l = max(l, max_l)
                l = 1
                
        return max(max_l, l)