from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maxValue(self, events, k):
        # Sort events by end day
        events.sort(key=lambda x: x[1])
        n = len(events)
        
        # Precompute previous non-overlapping event index for each event
        prev = [-1] * n
        ends = [e[1] for e in events]
        
        for i in range(n):
            # Find last event that ends before events[i] starts
            start = events[i][0]
            idx = bisect_right(ends, start - 1) - 1
            prev[i] = idx
        
        @lru_cache(None)
        def dp(i, rem):
            # Base case
            if i < 0 or rem == 0:
                return 0
            # Skip current event
            option1 = dp(i - 1, rem)
            # Take current event
            option2 = events[i][2] + dp(prev[i], rem - 1)
            return max(option1, option2)
        
        return dp(n - 1, k)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    events1 = [[1,2,4],[3,4,3],[2,3,1]]
    print(sol.maxValue(events1, 2))  # Output: 7

    events2 = [[1,2,4],[3,4,3],[2,3,10]]
    print(sol.maxValue(events2, 2))  # Output: 10

    events3 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
    print(sol.maxValue(events3, 3))  # Output: 9
