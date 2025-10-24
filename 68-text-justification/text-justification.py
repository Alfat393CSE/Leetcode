class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []  # Final result list to store justified lines
        cur = []  # Current line words
        num_of_letters = 0  # Total number of letters in current line (without spaces)

        for w in words:
            # Check if adding this word would exceed maxWidth
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Number of spaces to distribute
                spaces = maxWidth - num_of_letters
                if len(cur) == 1:
                    # If only one word, pad all spaces to the right
                    res.append(cur[0] + ' ' * spaces)
                else:
                    # Distribute spaces evenly
                    space_between_words = spaces // (len(cur) - 1)
                    extra_spaces = spaces % (len(cur) - 1)
                    line = ''
                    for i in range(len(cur) - 1):
                        # Leftmost slots get extra space first
                        line += cur[i] + ' ' * (space_between_words + (1 if i < extra_spaces else 0))
                    line += cur[-1]
                    res.append(line)
                # Reset for next line
                cur = []
                num_of_letters = 0
            # Add current word to line
            cur.append(w)
            num_of_letters += len(w)

        # Handle last line (left-justified)
        last_line = ' '.join(cur)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)

        return res
