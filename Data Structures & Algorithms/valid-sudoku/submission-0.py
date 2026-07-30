class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        position = [{"i":[],"j":[]} for i in range(9)]
        for i in range(9):
            for j in range(9):
                a = board[i][j]
                if a != ".":
                    position[int(a)-1]["i"].append(i+1)
                    position[int(a)-1]["j"].append(j+1)

        for p in position:
            i_s = p.get("i")
            j_s = p.get("j")
            i_3 = 0
            i_6 = 0
            i_9 = 0
            if(len(set(i_s))<len(i_s)):
                return False
            if(len(set(j_s))<len(j_s)):
                return False
            for k in range(len(i_s)):
                if i_s[k] in [1,2,3] and j_s[k] in [1,2,3]:
                    i_3 += 1
                if i_s[k] in [4,5,6] and j_s[k] in [4,5,6]:
                    i_6 += 1
                if i_s[k] in [7,8,9] and j_s[k] in [7,8,9]:
                    i_9 += 1
            if i_3 > 1 or i_6 > 1 or i_6 > 1:
                return False
        return True
                
        