class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for num in numSet:
            if (num - 1) not in numSet:
                lenght = 1
                while (num + lenght) in numSet:
                    lenght += 1
                longest = max(lenght,longest)
        return longest 
        