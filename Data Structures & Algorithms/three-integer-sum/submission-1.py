class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        output = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left = i + 1 
            right = len(nums) - 1

            while left < right:
                currSum = nums[left] + nums[i] + nums[right]
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    output.append([nums[left],nums[i],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return output 
        