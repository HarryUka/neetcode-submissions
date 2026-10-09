class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(i,curr_sum,curr_comb):
            if i >= len(nums) or curr_sum > target:
                return 
         
            if curr_sum == target:
                output.append(curr_comb.copy())
                return 

            curr_sum += nums[i]
            curr_comb.append(nums[i])

            backtrack(i,curr_sum,curr_comb)

            curr_sum -= nums[i]
            curr_comb.pop()

            backtrack(i + 1,curr_sum,curr_comb)

        backtrack(0,0,[])

        return output 


        