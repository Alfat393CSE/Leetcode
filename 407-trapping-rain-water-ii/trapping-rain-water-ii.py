import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        # Push all boundary cells into the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Process heap
        while heap:
            height, x, y = heapq.heappop(heap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # If neighbor is lower, water is trapped
                    res += max(0, height - heightMap[nx][ny])
                    # Update neighbor’s effective height
                    heapq.heappush(heap, (max(heightMap[nx][ny], height), nx, ny))

        return res
sol = Solution()
print(sol.trapRainWater([[1,4,3,1,3,2],
                         [3,2,1,3,2,4],
                         [2,3,3,2,3,1]]))  
# Output: 4

print(sol.trapRainWater([[3,3,3,3,3],
                         [3,2,2,2,3],
                         [3,2,1,2,3],
                         [3,2,2,2,3],
                         [3,3,3,3,3]]))  
# Output: 10
