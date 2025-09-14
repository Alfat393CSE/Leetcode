class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        
        vowels = set("aeiou")
        
        # Mask vowels with '*'
        def devowel(word):
            return "".join('*' if c in vowels else c for c in word)
        
        wordset = set(wordlist)  # For exact match
        
        # Case-insensitive dictionary (first occurrence matters)
        case_insensitive = {}
        
        # Vowel-masked dictionary (first occurrence matters)
        vowel_insensitive = {}
        
        for word in wordlist:
            lower = word.lower()
            if lower not in case_insensitive:
                case_insensitive[lower] = word
            masked = devowel(lower)
            if masked not in vowel_insensitive:
                vowel_insensitive[masked] = word
        
        result = []
        for q in queries:
            if q in wordset:
                result.append(q)  # exact match
            else:
                lower = q.lower()
                masked = devowel(lower)
                if lower in case_insensitive:
                    result.append(case_insensitive[lower])
                elif masked in vowel_insensitive:
                    result.append(vowel_insensitive[masked])
                else:
                    result.append("")
        
        return result

wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

print(Solution().spellchecker(wordlist, queries))
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
