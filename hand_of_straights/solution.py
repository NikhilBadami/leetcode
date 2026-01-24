class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        I'm given an integer, hand, which contains card numbers and a groupSize that I would like to use to rearrange the hand such that the
        hand can be divided into some number of groups where each group is of size groupSize and each group contains consecutive cards. This means
        that a card hand of [1,1,2] is invalid, but a hand of [1,2,3] is valid. The hand can be given in any order, so it would be useful to
        sort it first before attempting to solve the problem. Additionally, it would be good to see if the length of the hand can be evenly
        divided by groupSize; if it cannot, the problem cannot be solved. Note that consecutive means that the difference between
        consecutive cards can be at most 1

        Assuming a valid grouping is possible, I can iterate through the array and check every groupsize indices if the grouping is valid.
        If any group is invalid, return False, otherwise return True.

        time: O(nlog(n))
        memory: O(1)
        """
        # Check to see if the hand can even be divided evenly by groupSize
        if len(hand) % groupSize != 0:
            return False
        # Return true if the groupSize is 1 because it is always possible to divide any hand into groups of 1
        if groupSize == 1:
            return True
        
        # Sort the input hand
        hand.sort()

        # Attempt to form valid groups
        cur_group_start = 0
        cur_group_end = groupSize
        while cur_group_end <= len(hand):
            for i in range(cur_group_start+1, cur_group_end):
                if hand[i] == hand[i-1]:
                    return False
                if hand[i] - hand[i-1] > 1:
                    return False
            cur_group_start = cur_group_end + 1
            cur_group_end = cur_group_end + groupSize
        return True
        
