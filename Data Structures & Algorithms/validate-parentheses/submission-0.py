class Solution:
    def isValid(self, s: str) -> bool:

        dictionary = {"}":"{", "]":"[", ")": "("}

        stack = []


        for char in s:
            if char in dictionary:
                if stack and dictionary[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return stack == []

        