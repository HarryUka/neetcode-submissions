class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        

        output = []

        for mid , num in enumerate(nums):
            if num > 0:
                break

            if mid > 0 and num == nums[mid - 1]:
                continue

            left = mid + 1 
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[mid] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    output.append([nums[left],nums[mid],nums[right]])
                    left += 1
                    right -= 1 
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return output



        