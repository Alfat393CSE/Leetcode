class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        # Step 1: Combine and sort by position
        robots = sorted(zip(positions, healths, directions, range(n)))
        
        stack = []  # will store indices of robots moving right
        health = healths[:]  # copy to update
        
        for pos, h, d, idx in robots:
            if d == 'R':
                stack.append(idx)
            else:
                # d == 'L', check collision
                while stack and health[idx] > 0:
                    top = stack[-1]
                    
                    if health[top] < health[idx]:
                        # right robot dies
                        stack.pop()
                        health[idx] -= 1
                        health[top] = 0
                    elif health[top] > health[idx]:
                        # left robot dies
                        health[top] -= 1
                        health[idx] = 0
                        break
                    else:
                        # both die
                        stack.pop()
                        health[top] = 0
                        health[idx] = 0
                        break
        
        # Step 3: Collect survivors in original order
        result = []
        for i in range(n):
            if health[i] > 0:
                result.append(health[i])
        
        return result