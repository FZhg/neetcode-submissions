class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a freq map for the int
        # fill the list of num for each freq in the freq list of lenght n
        # count backward to collect k numbers

        result: List[int] = []
        freqMap: Dict[int, int] = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        
        freqList: List[List[int]] = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            freqList[freq].append(num)

        for nums in reversed(freqList):
            for num in nums:
                if len(result) == k:
                    # tie breaking by order in the num
                    return result
                result.append(num)

        return result