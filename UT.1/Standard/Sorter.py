f = open("Andmed.1/Andmed_ATI")
o = open("Andmed.1/Andmed_EKA")
k = open("Andmed.2/Andmed_Reaal_10.klass")
g = open("Andmed.2/Andmed_Reaal_11.klass")
b = open("Andmed.2/Andmed_Reaal_12.klass")
t = open("tulemused", "w")
u1 = []
d1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
u2 = []
d2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
u3 = []
d3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
u4 = []
d4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
u5 = []
d5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Vastused_1 = [1,0,1,1,0,0,1,0,0,1]
Vastused_2 = [1,1,0,0,1,0,1,0,0,1]
Täpsus = 0
Korduvus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def numbrid(q, Vastused, u, d):
    for a in q:
        counter = 0
        vastused = a.split()
        täpsus = 0
        global pikkus
        pikkus += 1
        for i in vastused:
            global Korduvus
            Korduvus[int(i)-1] = Korduvus[int(i)-1] + 1
            if int(i) > 5:
                if Vastused[counter] == 0:
                    täpsus += 1
                    d[counter] = d[counter] + 1
            elif int(i) < 6:
                if Vastused[counter] == 1:
                    täpsus += 1
                    d[counter] = d[counter] + 1
            counter += 1
        u.append(täpsus)

def king(r,l,ü,ö):
    global pikkus
    pikkus = 0
    numbrid(r,l,ü,ö)
    x = 0
    for a in ü:
        t.write(str(a) + ",")
    t.write("\n")
    for a in ö:
        t.write(str(int((((a)/pikkus)*100)).__round__()) + ",")
    t.write("\n")
    for i in ü:
        x += i
    global Täpsus
    Täpsus += x
    t.write(str(x))
    t.write("\n")

king(f,Vastused_1,u1,d1)
king(o,Vastused_1,u2,d2)
king(k,Vastused_2,u3,d3)
king(g,Vastused_2,u4,d4)
king(b,Vastused_2,u5,d5)
t.write(str(Täpsus))
t.write("\n")
t.write(str(Korduvus))