class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = []

        for i , temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                ind , temp_to_remove = stack.pop()
                output[ind] = i - ind
            stack.append((i,temp))

        return output 
        