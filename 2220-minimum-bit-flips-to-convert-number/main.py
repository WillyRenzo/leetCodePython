class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """Calculates the minimum number of bit flips to convert start to goal.

        Args:
            start: The starting integer.
            goal: The target integer.

        Returns:
            The minimum number of bit flips required.
        """

        # Count the number of bits that are different between start and goal
        diff = start ^ goal
        flips = 0

        # Count the number of 1 bits in the difference
        while diff != 0:
            flips += 1
            diff &= (diff - 1)

        return flips