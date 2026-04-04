class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if rows == 1:
            return encodedText  # No encoding needed
        
        n = len(encodedText)
        cols = n // rows  # Number of columns in the matrix
        
        # Reconstruct the matrix
        matrix = []
        for r in range(rows):
            matrix.append(list(encodedText[r*cols:(r+1)*cols]))
        
        # Read diagonally to recover originalText
        originalText = []
        for c in range(cols):
            row, col = 0, c
            while row < rows and col < cols:
                originalText.append(matrix[row][col])
                row += 1
                col += 1
        
        # Join and strip trailing spaces
        return ''.join(originalText).rstrip()