class Solution:
    def findLucky(self, arr):
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        lucky = -1
        for number, count in freq.items():
            if number == count:
                lucky = max(lucky, number)

        return lucky
