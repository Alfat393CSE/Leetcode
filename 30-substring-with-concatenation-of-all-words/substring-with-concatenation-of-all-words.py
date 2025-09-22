from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []
        
        # Iterate through s with sliding window shifts
        for i in range(word_len):  # try different offsets
            left = i
            seen = Counter()
            count = 0
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                if word in word_count:
                    seen[word] += 1
                    count += 1
                    # If we see more than required, shrink window
                    while seen[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                    # If valid window found
                    if count == len(words):
                        res.append(left)
                else:
                    # Reset window
                    seen.clear()
                    count = 0
                    left = j + word_len
        return res
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(Solution().findSubstring(s, words))  
# Output: [6, 9, 12]
