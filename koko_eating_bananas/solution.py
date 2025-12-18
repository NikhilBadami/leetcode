class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Need to find k, the rate at which koko can leisurely eat bananas before the guards return. I'm given a list of piles,
        which prepresent the amount of bananas in each piles, and h, the amount of time koko has before the guards return.
        For each pile, koko will eat at most k bananas. If k > piles[i], koko will only eat that pile for that hour. She
        will not  begin eating another pile.

        The parameter I'm searching for is k. I want to choose the smallest k such that koko can eat all bananas in h hours.
        Are there any limits on k? Yes, the largest pile in the piles array. There is no point in checking values beyond
        this pile, because koko will only ever eat one pile in an hour. So I know that k is bounded by (0, max(piles)]

        In a sense, I'm searching an "array" of values where the values are from 0 to max(piles) in increments of 1. The
        target is the smallest value k such that koko can eat all bananas in h hours. This means I will try multiple k's and
        record each valid answer as I find it, updating only when I find a smaller valid answer. This also means that for
        each candidate k, I need to loop through piles to check if the k is valid.

        I can search for k using a linear scan, which would be O(max(p) * n) where p represents values in piles and n is the
        number of piles. If I use binary search, however, this runtime improves significantly.

        time: O(log(max(p)) * n)
        memory: O(1)
        """
        import math
        # Get max possible k value
        max_p = max(piles)

        best_k = max_p
        l, r = 1, max_p
        # Search for valid k
        while l <= r:
            mid_pt = l + (r-l) // 2
            # Check if k is valid
            num_hours = 0
            for p in piles:
                # Get number of hours to eat given pile at candidate k
                num_hours += math.ceil(p / mid_pt)
            # Update search and best_k based on results
            if num_hours > h:
                # Took too long, need to try larger k values
                l = mid_pt + 1
            else:
                # Update k but keep searching for better values
                best_k = min(best_k, mid_pt)
                r = mid_pt - 1
        return best_k

