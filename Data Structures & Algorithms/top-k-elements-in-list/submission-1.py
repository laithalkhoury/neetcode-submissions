class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
                freq_map[n] = 1 + freq_map.get(n, 0)

        
        top_k_nums = []
        
        for i in range(k):
            curr_max = max(freq_map, key=freq_map.get)
            max_element = freq_map.pop(curr_max)
            top_k_nums.append(curr_max)

        return top_k_nums
