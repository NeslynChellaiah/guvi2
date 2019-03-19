class main:
    def func(self):
        a=int(input())
        count = 0
        while(a!=0):
            r=a%10
            count = count + (r*r)
            a=a//10
        print(count)
ob = main()
ob.func()
