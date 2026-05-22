class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {crs:[] for crs in range(numCourses)}

        for crs , prc in prerequisites:
            courseMap[crs].append(prc)

        taken = set()


        def canFinishHelper(crs):
            if crs in taken:
                return False 
            if courseMap[crs] == []:
                return True 
            
            taken.add(crs)
            
            for pre in courseMap[crs]:
                if not canFinishHelper(pre):
                    return False 
            
            taken.remove(crs)
            courseMap[crs] == []
            return True 


        for crs in range(numCourses):
            if not canFinishHelper(crs):
                return False 
        return True 





        

        