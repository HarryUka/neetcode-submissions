class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backTrack(i,comb,currSum):
            if i >= len(nums) or currSum > target:
                return 
            if currSum == target:
                res.append(comb.copy())
                return 
            # include i 

            comb.append(nums[i])
            backTrack(i,comb,currSum + nums[i])

            # exclude i 

            comb.pop()
            backTrack(i + 1,comb,currSum)

        backTrack(0,[],0)

        return res 


        