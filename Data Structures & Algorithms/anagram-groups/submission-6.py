class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)

        for s in strs:
            freq_list = [0] * 26
            for ch in s:
                freq_list[ord(ch) - ord('a')] += 1
            
            key = tuple(freq_list)
            freq_dict[key].append(s)
        
        return list(freq_dict.values())