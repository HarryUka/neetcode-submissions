class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNums = set(nums)
        longest = 0

        for i , num in enumerate(nums):
            if num - 1 not in setNums:
                lenght = 1
                while num + lenght in setNums:
                    lenght += 1
                longest = max(longest, lenght)

        return longest 
                
        