class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+ 1, r + 1]
            
            if numbers[l] + numbers[r] > target:
                # r is too big
                r -= 1
            
            else:
                # l is too small
                l += 1
            
            # invariant i and j is in [l, r]
            # prove by induction
        

        return []