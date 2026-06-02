class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        window_count = {}
        window_size = len(s1)
        for i in range(window_size):
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1
        if window_count == s1_count:
            return True
        for i in range(window_size, len(s2)):
            new_char = s2[i]
            window_count[new_char] = window_count.get(new_char, 0) + 1
            old_char = s2[i - window_size]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]
            if window_count == s1_count:
                return True
        return False