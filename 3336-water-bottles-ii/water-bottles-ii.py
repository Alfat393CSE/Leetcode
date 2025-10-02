class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # total bottles drunk
        total = 0  
        # empty bottles
        empty = 0  

        while numBottles > 0:
            # drink all current bottles
            total += numBottles
            empty += numBottles
            numBottles = 0

            # check if we can exchange
            if empty >= numExchange:
                empty -= numExchange  # spend numExchange empty bottles
                numBottles += 1       # gain 1 full bottle
                numExchange += 1      # exchange requirement increases

        return total
