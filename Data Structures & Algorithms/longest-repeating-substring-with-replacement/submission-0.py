class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = collections.defaultdict(int)

        left = 0 

        maxLen = float("-inf")


        for right in range(len(s)):
            dic[s[right]] += 1

            while (right - left + 1) - max(dic.values()) > k:
                dic[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen,right - left + 1)

        return maxLen 
        