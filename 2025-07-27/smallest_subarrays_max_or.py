class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n              # Default size is 1
        f = [-1] * 32              # Tracks latest position where each bit (0–31) was set

        for i in range(n - 1, -1, -1):  # Traverse from right to left
            t = 1
            for j in range(32):
                if (nums[i] >> j) & 1:  # If bit j is set in nums[i]
                    f[j] = i           # Update latest index of that bit
                elif f[j] != -1:       # If this bit exists to the right
                    t = max(t, f[j] - i + 1)  # Adjust required subarray length
            ans[i] = t
        return ans
