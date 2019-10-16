class Solution:
    def isMatchHelper(self, s: str, p: str) -> bool:
        if (not s and not p) or (len(p) == 1 and p[0] == "*"):
            return True
        elif (not p and s) or (not s and p):
            return False

        sc, pc = s[-1], p[-1]
        if sc == pc or pc == "?":
            return self.isMatchHelper(s[:-1], p[:-1])
        elif pc == "*":
            return self.isMatchHelper(s[:-1], p) or self.isMatchHelper(s, p[:-1])

        return False

    def isMatch(self, s: str, p: str) -> bool:
        while "**" in p:
            p = p.replace("**", "*")

        return self.isMatchHelper(s, p)


s = Solution()
assert not s.isMatch("aa", "a")
assert not s.isMatch("bc", "?a")
assert s.isMatch("adeceb", "a*b")
assert s.isMatch("adceb", "*a*b")
assert s.isMatch("a", "a*")
assert s.isMatch("ho", "**ho")
