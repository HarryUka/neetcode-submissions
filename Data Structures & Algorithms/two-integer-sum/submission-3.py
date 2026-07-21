class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = collections.defaultdict(int)

        for i , num in enumerate(nums):
            cum = target - num 
            if cum in seen:
                return [seen[cum],i]
            seen[num] = i 
        return []
        