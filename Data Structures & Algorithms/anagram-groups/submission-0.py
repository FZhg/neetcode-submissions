class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a fingerprint for each string a list of 26 letter with the value as freq. 
        # use the fingerprint as key to group string
        groups: Dict[List[int], List[str]] = defaultdict(list)

        for str in strs:
            fingerprint = [0] * 26
            for letter in str:
                fingerprint[ord(letter) - ord('a')] += 1
            groups[tuple(fingerprint)].append(str)


        return list(groups.values()) 
        