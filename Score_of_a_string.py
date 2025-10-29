class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(len(s)-1):
            curr = ord(s[i])
            next_curr = ord(s[i+1])
            difference = abs(curr- next_curr)
            score +=difference
        return score