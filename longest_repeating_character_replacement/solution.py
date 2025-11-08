class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Another way of framing this problem is what is the longest substring I can make with repeating characters
        assuming that I can replace a character up to k times. The string is up to 100000 characters and k <= len(s). s
        only contains upper case characters.

        I don't literally need to replace the characters in the string, I just need to know its possible to replace a
        character in a string. For example, say I have 'ABA' and k = 1. I just need to know I can replace the 'B' char
        and since I have k=1, I know that I can.

        One approach to this problem is to use a sliding window. Starting at the left of the string, I begin expanding
        the window by moving the right pointer. If the right pointer encounters a character differenct from the one
        at the left pointer, I check to see if I have any replacements remaining, and if I do, I decrement k and continue
        expanding the window.

        What do I do if I don't have any replacements? The obvious answer is to begin shrinking the window, but how do
        I go about increasing k? Say I have the string 'AABACCCA' and k = 1. Starting at the left of the string, I expand
        the window, and replace the first 'B' I encounter. However, when I get to 'C,' I am out of replacements, so I need
        to start shrinking the window. As I start shrinking, however, the first character I find is also an 'A' so it
        doesn't make sense to stop shriking there. So instead, I shrink the window until I find the first differing
        character, and then increase k.

        This would, however, leave me with the substring 'BAC,' which I can't make a valid solution using only 1
        replacement. So I would need to shrink the window until it is at most the size of the number of replacements
        I have available. So if k = 1, I shrink the window until it is of size 1.

        What if the string was 'AACACCCA'? The above paragraph is likely not right, instead what I should do is shrink
        the window until the left and right pointers point to the same character again.

        How do I increment k? Say I have 'AACCACCCA' and k = 2. Start with naieve solution of if the current character is
        different from the previous one as you are shrinking, increment k. Solution is max of the current window with the
        largest one found.

        time: O(n)
        memory: O(1)

        I could also keep track of the indices I replace, making the memory usage O(n) in the worst case
        """
        res = -1
        l, r = 0, 0
        replaced = set()

        while r < len(s):
            if s[r] == s[l]:
                r += 1
            elif s[r] != s[l]:
                if k >= 0:
                    k -= 1
                    replaced.add(r)
                    r += 1
                else:
                    res = max(res, r - l + 1)
                    while s[r] != s[l] and l != r:
                        if l in replaced:
                            k += 1
                            replaced.remove(l)
                        l += 1

        # Check if final points of l and r form a longer solutions
        res = max(res, r - l)
        return res
