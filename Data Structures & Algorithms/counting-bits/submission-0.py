class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        def get_bit_count(i):
            count = 0
            while i > 0:
                if i & 1 == 1:
                    count += 1 
                i = i >> 1
            return count 

        for i in range(n + 1):
            output.append(get_bit_count(i))
        return output 

        