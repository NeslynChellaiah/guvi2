class main:
    def func(self):
        e1,e2,K = input().split()
        K = int(K)
        e1=list(e1)
        e2=list(e2)
        count = 0
        l = len(e1)
        for i in range (0,l):
            if e1[i]!=e2[i]:
                count+=1
                print(count)
        if count==K:
            print("yes")
        else:
            print("no")
ob = main()
ob.func()
