# Leetcode 1971
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
# Easy

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        if source == destination:
            return True


        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()
        visited.add(source)


        def dfs(i):
            if i == destination:
                return True
            
            for n in graph[i]:
                if n not in visited:
                    visited.add(n)
                    if dfs(n):
                        return True

            return False
        
        return dfs(source)


