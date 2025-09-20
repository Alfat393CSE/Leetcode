from collections import deque, defaultdict
import bisect

class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit
        self.queue = deque()  # To store packets in FIFO order
        self.packet_set = set()  # To check for duplicates
        self.dest_dict = defaultdict(list)  # For counting by destination
        

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        
        # Remove oldest packet if memory limit is exceeded
        if len(self.queue) >= self.memoryLimit:
            old_packet = self.queue.popleft()
            self.packet_set.remove(old_packet)
            # Remove from dest_dict
            old_dest_list = self.dest_dict[old_packet[1]]
            old_index = bisect.bisect_left(old_dest_list, old_packet[2])
            if old_index < len(old_dest_list) and old_dest_list[old_index] == old_packet[2]:
                old_dest_list.pop(old_index)
        
        # Add new packet
        self.queue.append(packet)
        self.packet_set.add(packet)
        bisect.insort(self.dest_dict[destination], timestamp)
        return True
        

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.queue:
            return []
        
        packet = self.queue.popleft()
        self.packet_set.remove(packet)
        # Remove timestamp from dest_dict
        dest_list = self.dest_dict[packet[1]]
        index = bisect.bisect_left(dest_list, packet[2])
        if index < len(dest_list) and dest_list[index] == packet[2]:
            dest_list.pop(index)
        return [packet[0], packet[1], packet[2]]
        

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        dest_list = self.dest_dict.get(destination, [])
        left = bisect.bisect_left(dest_list, startTime)
        right = bisect.bisect_right(dest_list, endTime)
        return right - left
