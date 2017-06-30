import os
def Sts():
    while True:
        diie = raw_input("insert  the dirctory: ")
        os.system("clear")
        a = os.listdir(diie)
        te = len(a)
        print "the numbers we have in its dirctory", te
        print "#########################################"
        os.chdir(diie)
        for d in range(0,te):
            sd = os.path.getsize(a[d])
            print d,a[d],"size:",sd
Sts()