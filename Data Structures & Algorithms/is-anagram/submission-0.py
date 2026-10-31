class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter2Freq: Dict[string, int]  = defaultdict(int)

        # calculat the freq for s
        for letter in s:
            letter2Freq[letter] += 1

        # deduct freq for letters in t
        # if negative return false
        for letter in t:
            letter2Freq[letter] -= 1
            if letter2Freq[letter] < 0:
                return False
        

        # check if any freq is still positive
        # if so return false

        for freq in letter2Freq.values():
            if freq > 0:
                return False

        return True
