class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=[]
        z=0
        if x < 0:
            return False
        for i,j in enumerate(str(x)):
            y.append(int(j))
        for k, l in enumerate(y):
            a=l*(10**k)
            z=z+int(a)

        return z==x
