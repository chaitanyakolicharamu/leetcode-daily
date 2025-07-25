class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx = max(nums)
        if mx <= 0:
            return mx  # All elements are zero or negative

        ans = 0
        s = set()
        for x in nums:
            if x < 0 or x in s:
                continue  # Skip duplicates or negatives
            ans += x
            s.add(x)
        return ans
