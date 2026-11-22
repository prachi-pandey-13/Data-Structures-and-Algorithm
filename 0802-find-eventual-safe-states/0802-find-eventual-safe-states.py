class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # BFS
        V = len(graph)
        adj_list = [[] for _ in range(V)]
        indegrees = [0 for _ in range(V)]
        queue = deque()
        result = []
        for node in range(0,V):
            for adjNode in graph[node]:
                adj_list[adjNode].append(node)
                indegrees[node] += 1
        for i in range(0, V):
            if indegrees[i] == 0:
                queue.append(i)
        while len(queue) != 0:
            curr_node = queue.popleft()
            result.append(curr_node)
            for adjNode in adj_list[curr_node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)

        result.sort()
        return result


        
