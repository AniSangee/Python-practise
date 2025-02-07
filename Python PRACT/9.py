class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            if (num[i]+num[i+1]==target):
                print(i)

num=[2,7,11,15]
target=9
sol = Solution()
sol.twoSum(num,target)