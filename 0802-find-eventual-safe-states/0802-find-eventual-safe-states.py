class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V = len(graph)
        vis = [0 for _ in range(V)]
        pathvis = [0 for _ in range(V)]
        is_safe = [0 for _ in range(V)]
        for i in range(0,V):
            if vis[i] == 0:
                self.dfs(i, vis, pathvis, is_safe, graph)
        result = []
        for i in range(0,V):
            if is_safe[i] == 1:
                result.append(i)
        result.sort()
        return result

    def dfs(self, curr_node, vis, pathvis, is_safe, adj_list):
        vis[curr_node] = 1
        pathvis[curr_node] = 1
        for adjNode in adj_list[curr_node]:
            if vis[adjNode] == 0:
                ans = self.dfs(adjNode, vis, pathvis, is_safe, adj_list)
                if ans == False:
                    return False
            elif pathvis[adjNode] == 1:
                return False

        is_safe[curr_node] = 1
        pathvis[curr_node] = 0
        return True