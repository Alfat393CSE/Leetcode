class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for letter in phone_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res

print(Solution().letterCombinations("23"))
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(Solution().letterCombinations(""))
# []

print(Solution().letterCombinations("2"))
# ["a","b","c"]
