class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Step 1: Sort the intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]  # Initialize merged list with the first interval

        # Step 2: Iterate through the intervals
        for current in intervals[1:]:
            last = merged[-1]
            # Step 3: If current interval overlaps with last merged interval
            if current[0] <= last[1]:
                # Merge by updating the end of last interval
                last[1] = max(last[1], current[1])
            else:
                # If no overlap, simply append
                merged.append(current)

        return merged
