class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create hashmap
        # get map[a] = 0, 8 etc 
        # sort all the intervals 
        char_map = {}
        for i, char in enumerate(s):
            if char in char_map:
                char_map[char][1] = i
            else:
                char_map[char] = [i, i]
        
        sorted_intervals = sorted(char_map.values())
        # sorted_intervals = list(char_map.values())
        if len(sorted_intervals) == 1:
            return len(s)
        
        partitions = [sorted_intervals[0]]
        for interval in sorted_intervals:
            if interval[0] <= partitions[-1][1]:
                partitions[-1][1] = max(partitions[-1][1], interval[1])
            else:
                partitions.append(interval)
        for i, interval in enumerate(partitions):
            partitions[i] = interval[1] - interval[0] + 1
        
        return partitions
