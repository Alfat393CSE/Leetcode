class Spreadsheet(object):

    def __init__(self, rows):
        """
        Initialize spreadsheet with given number of rows and 26 columns (A-Z).
        Each cell starts with value 0.
        """
        self.rows = rows
        self.cols = 26  # A-Z
        # dictionary to store values explicitly set (row, col) -> value
        self.data = {}

    def _cellToIndex(self, cell):
        """
        Convert cell reference like 'A1' -> (row, col) as 0-indexed.
        """
        col = ord(cell[0]) - ord('A')   # 'A' -> 0, 'B' -> 1, ...
        row = int(cell[1:]) - 1         # row is 1-indexed in input
        return (row, col)

    def setCell(self, cell, value):
        """
        Sets the value of the specified cell.
        """
        row, col = self._cellToIndex(cell)
        self.data[(row, col)] = value

    def resetCell(self, cell):
        """
        Resets the specified cell to 0.
        """
        row, col = self._cellToIndex(cell)
        if (row, col) in self.data:
            del self.data[(row, col)]   # removing means value defaults to 0

    def _getCellValue(self, cell):
        """
        Returns value of a cell reference or integer string.
        """
        if cell.isdigit():   # If it's a plain number
            return int(cell)
        row, col = self._cellToIndex(cell)
        return self.data.get((row, col), 0)

    def getValue(self, formula):
        """
        Evaluates formula of the form '=X+Y'
        where X and Y are either cell refs or integers.
        """
        # strip '=' and split by '+'
        parts = formula[1:].split('+')
        val1 = self._getCellValue(parts[0])
        val2 = self._getCellValue(parts[1])
        return val1 + val2
spreadsheet = Spreadsheet(3)

print(spreadsheet.getValue("=5+7"))  # 12
spreadsheet.setCell("A1", 10)
print(spreadsheet.getValue("=A1+6"))  # 16
spreadsheet.setCell("B2", 15)
print(spreadsheet.getValue("=A1+B2"))  # 25
spreadsheet.resetCell("A1")
print(spreadsheet.getValue("=A1+B2"))  # 15
