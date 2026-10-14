class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            num = nums[i]
            cum = target - num

            if cum in hashMap:
                return [hashMap[cum],i]
            hashMap[num] = i 
        return []


        