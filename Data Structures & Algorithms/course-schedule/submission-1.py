class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        for i in range(numCourses):
            courses[i] = []
        for i, j in prerequisites:
            courses[i].append(j)
    
        def dfs(course,visited):
            if course in visited:
                return False
            if course not in courses or courses[course] == []:
                return True
            visited.add(course)
            for req in courses[course]:
                if dfs(req,visited) == False:
                    return False
            visited.remove(course)
            del courses[course]

        for i in range(numCourses):
            if i in courses:
                if dfs(i,set()) == False:
                    return False
        return True