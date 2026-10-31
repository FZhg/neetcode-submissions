class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            res.append(string)
        return "".join(res)



    def decode(self, s: str) -> List[str]:
        result: List[str] = []
        
        i: int = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            string = s[j + 1: j + length + 1]
            result.append(string)
            i = j + length + 1
        

        return result