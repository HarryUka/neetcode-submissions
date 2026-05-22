class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            left = i + 1
            right = len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1

                else:
                    output.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right - 1] and left < right:
                        right -= 1
        return output 
        