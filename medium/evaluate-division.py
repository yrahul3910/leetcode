# https://leetcode.com/problems/evaluate-division/
from typing import List
from collections import deque


class Solution:
    cache = {}
    def bfs(self, graph, visited, src, dst):
        if src not in graph or dst not in graph:
            return -1.

        d = {src: 1}

        q = deque([src])
        while len(q):
            u = q.popleft()

            if (u, dst) in self.cache:
                return d[u] * self.cache[(u, dst)]

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    d[v] = d[u] * graph[u][v]
                    q.appendleft(v)

                    self.cache[(src, v)] = d[v]
                if v == dst:
                    return d[v]
        return -1.

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        visited = {}
        self.cache = {}

        for [src, dst], v in zip(equations, values):
            if src in graph:
                graph[src][dst] = v
            else:
                graph[src] = {dst: v}
                visited[src] = False
            if dst in graph:
                graph[dst][src] = 1. / v
            else:
                graph[dst] = {src: 1. / v}
                visited[dst] = False
        
        results = []
        for [src, dst] in queries:
            # Perform BFS
            visited = {x: False for x in visited}
            visited[src] = True
            
            results.append(self.bfs(graph, visited, src, dst))
        
        return results

