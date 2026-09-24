from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)] 

        for num, freq in count.items():
            buckets[freq].append(num) # multiple nums in the same buckets

        ret = []
        for cls in range(len(buckets)-1, -1, -1):
            for num in buckets[cls]:
                ret.append(num)
                if len(ret) == k:
                    return ret
        return ret
        
        

        