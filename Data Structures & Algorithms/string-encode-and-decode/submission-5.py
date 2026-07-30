class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return "None"
        else:
            return "^~".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        return s.split('^~')
