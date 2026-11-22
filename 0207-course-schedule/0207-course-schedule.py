class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        queue = deque()
        result = []
        for u, v in prerequisites:
            adj_list[u].append(v)
            indegrees[v] += 1

        for i in range(0,numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while len(queue) != 0:
            curr_node = queue.popleft()
            result.append(curr_node)
            for adjNode in adj_list[curr_node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)
        
        if len(result) == numCourses:
            return True
        return False