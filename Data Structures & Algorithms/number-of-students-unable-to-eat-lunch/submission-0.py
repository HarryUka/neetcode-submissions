class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        count = Counter(students)

        for pref in sandwiches:
        
            if count[pref] > 0:
                count[pref] -= 1
                res -= 1
            else:
                return res 
            

        return res 
        