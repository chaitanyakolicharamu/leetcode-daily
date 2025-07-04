class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        n = len(operations)
        lengths = [1] * (n + 1)  # length after each step

        # Step 1: Track length of the string after each operation
        for i in range(n):
            lengths[i + 1] = lengths[i] * 2

        shifts = 0

        # Step 2: Walk backwards to trace origin of character at position k
        for i in reversed(range(n)):
            half = lengths[i]
            if k > half:
                k -= half  # Now we're in the first half again
                if operations[i] == 1:
                    shifts += 1  # It was a shifted copy
            # else: it came from the first half — nothing changes

        # Step 3: Start with 'a' and apply shifts
        return chr((ord('a') - ord('a') + shifts) % 26 + ord('a'))