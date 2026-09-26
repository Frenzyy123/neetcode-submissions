class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        conditions = {}
        visited_small = set()
        for i,j in prerequisites:
            if i not in conditions:
                conditions[i] = []
            conditions[i].append(j)
        def dfs(course):
            if course in visited_small:
                return False
            if course not in conditions:
                return True
            visited_small.add(course)
            for c in conditions[course]:
                if dfs(c) == False:
                    return False
            visited_small.remove(course)
            del conditions[course]


        for i in range(numCourses):
            if i not in conditions:
                continue
            if dfs(i) == False:
                return False
        return True
            
