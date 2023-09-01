class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        numsD = {}

        for i in range(len(nums)):
            if nums[i] in numsD:
                return True
            else:
                numsD[nums[i]] = 1
        

