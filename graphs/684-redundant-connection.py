'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
'''

from collections import defaultdict


class Solution: 
    def findRedundantConnection(edges: list[list[int]]) -> list[int]:
        ### create a dictionary of 
        graph = defaultdict(set)

        def dfs(current, end, visited_nodes):
            visited_nodes.add(current)

            if current == end:
                return True

            for neighbor in graph[current]:
                if neighbor not in visited_nodes:
                    if dfs(neighbor, end, visited_nodes):
                        return True
        
            return False



        for u, v in edges: 
            if u in graph and v in graph and dfs(u, v, set()):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)
            


test_case = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(Solution.findRedundantConnection(test_case))