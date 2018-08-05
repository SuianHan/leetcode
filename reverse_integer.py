class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        y=[]
        z=0
        b=0
        if x < 0:
            x=abs(x)
            b=1
        for i,j in enumerate(str(x)):
            y.append(int(j))
        for k, l in enumerate(y):
            x=l*(10**k)
            z=z+int(x)
        if b==1:
            z=-z
        if z < -2**31 or z > 2**31-1:
            z=0
        return z