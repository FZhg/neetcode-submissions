class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result: int = 0
        visited = set()
        numSet = set(nums)
        for num in numSet:
            if num - 1 in numSet:
                # not a start of seq
                continue
            if num in visited:
                # all formed the seq
                continue 
            seq = self.buildSeq(numSet, num)
            visited.update(seq)
            if len(seq) > result:
                result = len(seq)
        
        return result

    
    def buildSeq(self, numSet: Set[int], start: int) -> List[int]:
        seq: List[int] = []
        curr = start
        while curr in numSet:
            seq.append(curr)
            curr += 1
        return seq
