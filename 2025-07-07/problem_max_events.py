import heapq

class Solution:
    def maxEvents(self, events):
        events.sort()
        total_days = 0
        day = 0
        i = 0
        n = len(events)
        min_heap = []

        while i < n or min_heap:
            if not min_heap:
                day = events[i][0]

            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                total_days += 1
                day += 1
            else:
                if i < n:
                    day = events[i][0]

        return total_days
