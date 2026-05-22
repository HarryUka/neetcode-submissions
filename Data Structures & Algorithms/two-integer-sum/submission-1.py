class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = collections.defaultdict(int)

        for ind , num in enumerate(nums):
            cum  = target - num

            if cum in seen:
                return [seen[cum],ind]

            seen[num] = ind
        return []

            

        
        