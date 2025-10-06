class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # Sort to handle duplicates
        visited = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                # Skip duplicates
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue

                visited[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                visited[i] = False

        backtrack([])
        return res
