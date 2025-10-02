class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        candidates.sort()  # Sort to handle duplicates easily

        def backtrack(start, path, remaining):
            if remaining == 0:
                results.append(list(path))
                return
            if remaining < 0:
                return

            prev = -1
            for i in range(start, len(candidates)):
                # Skip duplicates at the same level
                if candidates[i] == prev:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return results
