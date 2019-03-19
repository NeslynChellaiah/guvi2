class main:
    def fun(self):
        a = int(input())
        fac = 1
        for i in range (0,a):
            fac = fac*a
            a=a-1
        print (fac)
ob=main()
ob.fun()
