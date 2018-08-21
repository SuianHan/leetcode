class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        elif len(s) >= 2:
            for i, j in enumerate(s[:-1]):
                if j == '(' and s[i + 1] == ')':
                    return self.isValid(self,s[:i] + s[i + 2:])
                elif j == '[' and s[i + 1] == ']':
                    return self.isValid(self,s[:i] + s[i + 2:])
                elif j == '{' and s[i + 1] == '}':
                    return self.isValid(self,s[:i] + s[i + 2:])
            return False
        else:
            return False
