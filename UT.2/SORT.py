import math
f = open("/Users/ukuoliverahven/PycharmProjects/School_go_BRRRRRR/UT.1/Standard/Andmed.1/Andmed_ATI")
o = open("/Users/ukuoliverahven/PycharmProjects/School_go_BRRRRRR/UT.1/Standard/Andmed.1/Andmed_EKA")
k = open("/Users/ukuoliverahven/PycharmProjects/School_go_BRRRRRR/UT.1/Standard/Andmed.2/Andmed_Reaal_10.klass")
g = open("/Users/ukuoliverahven/PycharmProjects/School_go_BRRRRRR/UT.1/Standard/Andmed.2/Andmed_Reaal_11.klass")
b = open("/Users/ukuoliverahven/PycharmProjects/School_go_BRRRRRR/UT.1/Standard/Andmed.2/Andmed_Reaal_12.klass")
F = open("Tulemused_vol_ATi.csv", "w")
B = open("Tulemused_vol_EKA.csv", "w")
I = open("Tulemused_vol_10.csv", "w")
C = open("Tulemused_vol_11.csv", "w")
A = open("Tulemused_vol_12.csv", "w")

Õilaste_Täpsused = []
Küsimuste_täpsused = [0,0,0,0,0,0,0,0,0,0]
Iga_küsimus = [

]
Vastused_1 = [1,0,1,1,0,0,1,0,0,1]
Vastused_2 = [1,1,0,0,1,0,1,0,0,1]
Täpsus = 0


"""
ÕT = Õpilase_Täpsus
KT = Küsimuse_Täpsus
Counter on selleks, et jälgida KT indeksit
Täpsus on selleks, et seda hiljem ÕT listi lisada
"""
def numbrid(fail, Vastused, ÕT, KT):
    for a in fail:
        counter = 0
        vastused = a.split()
        täpsus = 0
        for i in vastused:
            global Korduvus
            if int(i) > 5:
                if Vastused[counter] == 0:
                    täpsus += (int(i) * 0.2 - 1)
                    KT[counter] = round(KT[counter] + (int(i) * 0.2 - 1), 2)
                    Iga_küsimus[counter].append(round((int(i) * 0.2 - 1), 2))
                else:
                    Iga_küsimus[counter].append(0)
            elif int(i) < 6:
                if Vastused[counter] == 1:
                    täpsus += 1 - (int(i) - 1) * 0.2
                    KT[counter] = round(KT[counter] + (1 - (int(i) - 1) * 0.2), 2)
                    Iga_küsimus[counter].append(round(((int(i) - 1) * 0.2), 2))
                else:
                    Iga_küsimus[counter].append(0)
            counter += 1
        ÕT.append(round(täpsus,2))

def king(r,l,ü,ö,t):
    global Õilaste_Täpsused
    global Küsimuste_täpsused
    global Iga_küsimus
    Õilaste_Täpsused = []
    Küsimuste_täpsused = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Iga_küsimus = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    numbrid(r,l,ü,ö)
    x = 0
    for a in ü:
        t.write(str(a) + ",")
    t.write("\n")
    t.write(str(ö))
    t.write("\n")
    for a in range(len(Iga_küsimus)):
        t.write(str(Iga_küsimus[a]).strip("[""]"))
        t.write("\n")
    for i in ü:
        x += i
    global Täpsus
    Täpsus += x
    t.write(str(round(x, 2)))
    t.write("\n")

king(f,Vastused_1,Õilaste_Täpsused,Küsimuste_täpsused, F)
king(o,Vastused_1, Õilaste_Täpsused,Küsimuste_täpsused, B)
king(k,Vastused_2,Õilaste_Täpsused,Küsimuste_täpsused, I)
king(g,Vastused_2,Õilaste_Täpsused,Küsimuste_täpsused, C)
king(b,Vastused_2,Õilaste_Täpsused,Küsimuste_täpsused, A)
