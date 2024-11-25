'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ### List of boolean values indicating whether course can be finished
        can_finish_list = [False for _ in range(numCourses)]
        ### make adjacnecy list 
        graph = [[] for _ in range(numCourses)]

        for course, dependency in prerequisites:
            graph[course].append(dependency)
        
        ### set to keep track of nodes in current dependency path
        path = set()
        print(graph)
        def dfs(course):
            if course in path:
                return False
            if not graph[course] or can_finish_list[course]:
                can_finish_list[course] = True
                return True 
            path.add(course)
            for dependency in graph[course]:
                if not dfs(dependency):
                    return False
            can_finish_list[course] = True
            path.remove(course)
            return True

        ### dfs on all nodes 
        for course in range(numCourses):
            if can_finish_list[course]:
                continue
            if not dfs(course):
                return False
        return True
