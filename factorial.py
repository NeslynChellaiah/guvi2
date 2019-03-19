class main:
    def func(self):
        a = int(input())
        fac = 1
        for i in range (0,a):
            fac=fac*a
            a-=1
        print (fac)
ob =  main()
ob.func()
