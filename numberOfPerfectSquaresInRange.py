import math
class main:
    def func(self,i,j):
        count = 0
        for i in range (i,j+1):
            b=i
            i = math.sqrt(i)
            if (i-math.floor(i)==0):
                count+=1
        print(count)
ob = main()
i,j=input().split()
i = int(i)
j = int(j)
ob.func(i,j)
