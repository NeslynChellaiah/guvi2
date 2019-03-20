class main():
    def func(self):
        a,b = input().split()
        a = int(a)
        b = int(b)
        if a<b:
            small = a
        else:
            small = b
        for i in range (1,small+1):
            if (a%i==0) and (b%i==0):
                gcd = i
        print (gcd)
ob = main()
ob.func()
