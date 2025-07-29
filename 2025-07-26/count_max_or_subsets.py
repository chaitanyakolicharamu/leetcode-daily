class Solution:
  def countMaxOrSubsets(self, nums: list[int]) -> int:
    ors = functools.reduce(operator.or_, nums)  # Global max OR from all elements
    ans = 0

    def dfs(i: int, path: int) -> None:
      nonlocal ans
      if i == len(nums):
        if path == ors:
          ans += 1
        return

      dfs(i + 1, path)                # Skip current element
      dfs(i + 1, path | nums[i])     # Include current element

    dfs(0, 0)
    return ans
