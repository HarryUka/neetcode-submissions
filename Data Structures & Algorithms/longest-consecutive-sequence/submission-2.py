class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        setNums = set(nums)


        for i in range(len(nums)):
            if  nums[i] - 1 not in setNums:
                length = 1
                while nums[i] + length in setNums:
                    length += 1 
                longest = max(longest,length)

        return longest 

                