class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1

        queue = deque()
        taken = set()

        for crs in range(numCourses):
            if in_degree[crs] == 0:
                queue.append(crs)
        
        while queue:
            curr_crs = queue.popleft()
            taken.add(curr_crs)

            for crs in adj[curr_crs]:
                in_degree[crs] -= 1
                if in_degree[crs] == 0:
                    queue.append(crs)

        return len(taken) == numCourses