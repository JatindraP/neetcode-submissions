class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for item in strs:
            encoded = encoded+item+'|'
        return encoded

    def decode(self, s: str) -> List[str]:
        return s.split('|')[:-1]
