class Solution:
    def findOrder(self,numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        prereqs = {}
        visited = set()
        for i in range(numCourses):
            if i not in prereqs:
                prereqs[i] = []
        for pre in prerequisites:
            prereqs[pre[0]].append(pre[1])
        def dfs(curr,visited:set):
            if curr not in prereqs:
                return True
            if curr in visited:
                return False
            visited.add(curr)
            for pre in prereqs[curr]:
                if dfs(pre,visited) == False:
                    return False
            output.append(curr)
            del prereqs[curr]
            return True

        for i in range(numCourses):
            if i not in prereqs:
                continue
            if dfs(i,visited) == False:
                return []
        return output
