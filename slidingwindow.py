class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window
        window = set()
        i, j, ans = 0, 0, 0
        while i < len(s) and j < len(s):
            if s[j] not in window:
                window.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                window.remove(s[i])
                i += 1
                
        return ans