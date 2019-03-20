class main():
    def func(self):
        a,b=input().split()
        c,d=input().split()
        e,f=input().split()
        if (a==c==e) or (b==d==f):
            print ("yes")
        else:
            print ("no")
ob = main()
ob.func()
