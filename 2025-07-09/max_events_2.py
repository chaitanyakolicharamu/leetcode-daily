class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        max_gap_before, max_free_time, last_end = 0, 0, 0

        for i in range(n):
            meeting_time = endTime[i] - startTime[i]
            next_start = eventTime if i == n - 1 else startTime[i + 1]
            free_time = next_start - last_end
            if meeting_time > max_gap_before:
                free_time -= meeting_time
            max_free_time = max(max_free_time, free_time)
            max_gap_before = max(max_gap_before, startTime[i] - last_end)
            last_end = endTime[i]

        max_gap_after, last_start = 0, eventTime
        for i in reversed(range(n)):
            meeting_time = endTime[i] - startTime[i]
            prev_end = 0 if i == 0 else endTime[i - 1]
            free_time = last_start - prev_end
            if meeting_time <= max_gap_after:
                max_free_time = max(max_free_time, free_time)
            max_gap_after = max(max_gap_after, last_start - endTime[i])
            last_start = startTime[i]

        return max_free_time

