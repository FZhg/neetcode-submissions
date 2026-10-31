class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist: Dict[int, bool] = defaultdict(bool)

        for num in nums:
            if exist[num]:
                return True
            exist[num] = True
        return False