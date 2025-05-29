Bench = []
Bench2 = ["1","2","3"]

P1 = "B1"
P2 = "B2"
P3 = "G"

flag = ""

def popping():
    global flag
    if Bench[0] == Bench[1] or Bench[1] == "G":
        Bench.pop()
        flag = "invalid"
    else:
        flag = "valid"

def poppingBench2():
    global flag
    if Bench2[0] == Bench2[1] or Bench2[0] == Bench2[2] or Bench2[1] == Bench2[2]:
        Bench2.pop()
        flag = "invalid"
    else:
        flag = "valid"

def valid(P1, P2):
    global Bench2
    if flag == "valid":
        Bench2 = []
        Bench2.append(P1)
        Bench2.append(P2)

def Bench1Check(P1, P2, P3):
    Bench.append(P1)
    Bench.append(P1)
    popping()
    if flag == "valid":
        valid(P1, P1)
        Bench.pop()
        Bench2Check(P1, P2, P3)
    Bench.append(P2)
    popping()
    if flag == "valid":
        valid(P1, P2)
        Bench.pop()
        Bench2Check(P1, P2, P3)
    Bench.append(P3)
    popping()
    if flag == "valid":
        valid(P1, P3)
        Bench2Check(P1, P2, P3)

def Bench2Check(P1, P2, P3):
    Bench2.append(P1)
    poppingBench2()
    if flag == "valid":
        print("Valid Bench", Bench2)
    if len(Bench2) < 3:
        Bench2.append(P2)
        poppingBench2()
        if flag == "valid":
            print("Valid Bench", Bench2)
    if len(Bench2) < 3:
        Bench2.append(P3)
        poppingBench2()
        if flag == "valid":
            print("Valid Bench", Bench2)

Holder = ""

for i in range(3):
    Bench = []
    Bench2 = []
    Bench1Check(P1, P2, P3)
    Holder = P1
    P1 = P2
    P2 = P3
    P3 = Holder

