'''
'''
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        schedule = []

        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node):

            for prerequisite in graph[node]:
                if prerequisite not in visited:
                    dfs(prerequisite)
            schedule.append(node)
            visited.add(node)


        
        for node in graph:
            if node not in visited:
                dfs(node)

        return schedule