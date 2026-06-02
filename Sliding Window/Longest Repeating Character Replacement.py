class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = {}
        left = 0
        max_len = 0
        max_freq = 0
        for right in range(len(s)):
            my_dict[s[right]] = my_dict.get(s[right], 0) + 1
            max_freq = max(max_freq, my_dict[s[right]])
            if (right - left + 1) - max_freq > k:
                my_dict[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len