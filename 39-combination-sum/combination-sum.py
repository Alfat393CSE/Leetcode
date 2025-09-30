class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])  # Found valid combination
                return
            if total > target:
                return  # Overshot target, stop here

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # i, not i+1 — numbers can repeat
                path.pop()  # Backtrack

        backtrack(0, [], 0)
        return result
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
# Output: [[2, 2, 3], [7]]

print(sol.combinationSum([2,3,5], 8))
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

print(sol.combinationSum([2], 1))
# Output: []
