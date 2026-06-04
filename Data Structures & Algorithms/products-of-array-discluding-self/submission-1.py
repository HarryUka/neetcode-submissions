class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        output = []
        p1 =  1

        for i in range(len(nums)):
            output.append(p1)
            p1 =  p1 * nums[i]

        p1 = 1 

        for i in range(len(nums) -1, -1, -1):
            output[i] = output[i] * p1 
            p1 = p1 * nums[i]
        return output  
        


        