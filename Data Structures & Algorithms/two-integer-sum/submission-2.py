class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}


        for i , num in enumerate(nums):
            cum = target - num
            if cum in seen:
                return [seen[cum], i]

            if num not in seen:
                seen[num] = i
        return []
        