class main:
    def func(self):
        e1,e2,K = input().split()
        e1=[x for x in e1.split()]
        e2=[x for x in e2.split()]
        count = 0
        for item in e1:
            if item in e2:
                return
            else:
                count += 1
        if count==K:
            print("yes")
        else:
            print("no")
ob = main()
ob.func()
