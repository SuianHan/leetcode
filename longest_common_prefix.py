class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a = strs
        astr = ''
        b = ''

        if a==[]:
            return b
        elif min(a)=='' or len(a)==0:
            return b
        elif len(a)==1:
            b=a[0]
            return b
        elif len(a)==2:
            if len(a[0]) < len(a[1]):
                astr = a[0]
            else:
                astr = a[1]
            for i,j in enumerate(astr):
                if a[0][i] == a[1][i]:
                    b += a[0][i]
                else:
                    break
            return b
        else:
            astr = a[0]
            for i in range(len(a)):
                if i > 0:
                    if len(a[i]) < len(astr):
                        astr = a[i]
                else:
                    if len(a[i]) < len(a[i + 1]):
                        astr = a[i]
            for i,j in enumerate(astr):
                c = a[0][i]
                for k in range(len(a)):
                    if a[k][i] == c:
                        d = a[k][i]
                    else:
                        d=''
                        break
                b += d

            return b


a=["flower","flow","flight"]
a1=["aca","cba"]
sol=Solution
print(sol.longestCommonPrefix(sol,a1))