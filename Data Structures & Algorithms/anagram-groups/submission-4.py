class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)

        for s in strs:
            countS = {}
            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
        
            key = tuple(sorted(countS.items()))
            freq_dict[key].append(s)
        
        
        

        return list(freq_dict.values())
