from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        en_uzun_seri = 0
        for num in num_set:
            if (num - 1) not in num_set:
                su_anki_sayi = num
                su_anki_seri = 1
                while (su_anki_sayi + 1) in num_set:
                    su_anki_sayi += 1
                    su_anki_seri += 1
                en_uzun_seri = max(en_uzun_seri, su_anki_seri)
        return en_uzun_seri