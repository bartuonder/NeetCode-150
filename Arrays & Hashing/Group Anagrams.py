from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDictionary = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in myDictionary:
                myDictionary[key].append(s)
            else:
                myDictionary[key] = [s]
        return list(myDictionary.values())