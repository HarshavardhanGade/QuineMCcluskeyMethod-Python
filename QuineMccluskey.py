
from itertools import combinations
nob = int(input("ENTER NUMBER OF BITS\n"))
f = set(map(int, input("ENTER MINTERMS\n").split(',')))
x = 2 ** nob
if max(f) >= x:
 print(max(f), "IS OUT OF", nob, "BIT RANGE")
else:
 g0 = {0}
 g1 = {1, 2, 4, 8, 16, 32, 64, 128}
 g2 = {3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48, 64, 66, 
72, 80, 96, 129, 130, 132, 136, 144, 160, 192}
 g3 = {7, 11, 13, 14, 19, 21, 22, 25, 26, 28, 35, 37, 38, 41, 42, 44, 
49, 50, 52, 56, 67, 69, 70, 73, 74, 76, 81, 82,
 84, 88, 97, 98, 100, 104,
 112, 131, 133, 134, 137, 138, 140, 145, 146, 148, 152, 161, 162, 
164, 168, 176, 193, 194, 196, 200, 208, 224}
 g4 = {15, 23, 27, 29, 30, 39, 43, 45, 46, 51, 53, 54, 57, 58, 60, 72, 
75, 77, 78, 83, 85, 86, 89, 90, 92, 99, 101,
 102, 105, 106, 108, 113,
 114, 116, 120, 135, 139, 141, 142, 147, 149, 150, 153, 154, 156, 
163, 165, 166, 169, 170, 172, 177, 178, 180,
 184, 195, 197,
 198, 201, 202, 204, 209, 210, 212, 216, 225, 226, 228, 232, 240}
 g5 = {31, 47, 55, 59, 61, 62, 79, 87, 91, 93, 94, 103, 107, 109, 110, 
115, 117, 118, 121, 122, 124, 143, 151, 155,
 157, 158, 167, 171,
 173, 174, 179, 181, 182, 185, 186, 188, 199, 203, 205, 206, 211, 
213, 214, 217, 218, 220, 227, 229, 230, 233,
 234, 236, 241, 242,
 244, 248}
 g6 = {63, 95, 111, 119, 123, 125, 126, 159, 175, 183, 187, 189, 190, 
207, 215, 219, 221, 222, 231, 235, 237, 238,
 243, 245, 246, 249,
 250, 252}
 g7 = {127, 191, 223, 239, 247, 251, 253, 254}
 g8 = {255}
 G0 = []
 G1 = []
 G2 = []
 G3 = []
 G4 = []
 G5 = []
 G6 = []
 G7 = []
 G8 = []
 # GROUPING
 grp0 = list(g0.intersection(f))
 grp0.sort()
 grp1 = list(g1.intersection(f))
 grp1.sort()
 grp2 = list(g2.intersection(f))
 grp2.sort()
 grp3 = list(g3.intersection(f))
 grp3.sort()
 grp4 = list(g4.intersection(f))
 grp4.sort()
 grp5 = list(g5.intersection(f))
 grp5.sort()
 grp6 = list(g6.intersection(f))
 grp6.sort()
 grp7 = list(g7.intersection(f)) grp5.sort()
 grp8 = list(g8.intersection(f))
 grp8.sort()
 l0 = len(grp0)
 l1 = len(grp1)
 l2 = len(grp2)
 l3 = len(grp3)
 l4 = len(grp4)
 l5 = len(grp5)
 l6 = len(grp6)
 l7 = len(grp7)
 l8 = len(grp8)
 # GROUP 0 CONVERSION
 if l0 != 0:
 for i in range(l0):
 d0 = bin(grp0[i])
 d0 = d0[2::]
 s = ""
 for i in range(nob - len(d0)):
 s = s + "0"
 s = s + d0
 G0.append(s)
 # print("G0 = ", G0)
 # GROOUP 1 CONVERSION
 if l1 != 0:
 for i in range(l1):
 d1 = bin(grp1[i])
 d1 = d1[2::]
 s = ""
 for j in range(nob - len(d1)):
 s = s + "0"
 s = s + d1
 G1.append(s)
 # print("G1 = ", G1)
 # GROUP 2 CONVERSION
 if l2 != 0:
 for i in range(l2):
 d2 = bin(grp2[i])
 d2 = d2[2::]
 s = ""
 for j in range(nob - len(d2)):
 s = s + "0"
 s = s + d2
 G2.append(s)
 # print("G2 = ", G2)
 # GROUP 3 CONVERSION
 if l3 != 0:
 for i in range(l3):
 d3 = bin(grp3[i])
 d3 = d3[2::]
 s = ""
 for i in range(nob - len(d3)):
 s = s + "0"
 s = s + d3
 G3.append(s)
 # print("G3 = ", G3)
 # GROUP 4 CONVERSION
 if l4 != 0:
 for i in range(l4):
 d4 = bin(grp4[i])
 d4 = d4[2::] s = ""
 for i in range(nob - len(d4)):
 s = s + "0"
 s = s + d4
 G4.append(s)
 # print("G4 = ", G4)
 # GROUP 5 CONERSION
 if l5 != 0:
 for i in range(l5):
 d5 = bin(grp5[i])
 d5 = d5[2::]
 s = ""
 for i in range(nob - len(d5)):
 s = s + "0"
 s = s + d5
 G5.append(s)
 # print("G5 = ", G5)
 # GROUP 6 CONVERSION
 if l6 != 0:
 for i in range(l6):
 d6 = bin(grp6[i])
 d6 = d6[2::]
 s = ""
 for i in range(nob - len(d6)):
 s = s + "0"
 s = s + d6
 G6.append(s)
 # print("G6 = ", G6)
 # GROUP 7 CONVERSION
 if l7 != 0:
 for i in range(l7):
 d7 = bin(grp7[i])
 d7 = d7[2::]
 s = ""
 for i in range(nob - len(d7)):
 s = s + "0"
 s = s + d7
 G7.append(s)
 # print("G7 = ", G7)
 # GROUP 8 CONVERSION
 if l8 != 0:
 for i in range(l8):
 d8 = bin(grp8[i])
 d8 = d8[2::]
 s = ""
 for i in range(nob - len(d8)):
 s = s + "0"
 s = s + d8
 G8.append(s)
 # print("G8 = ", G8)
def convert(a):
 b = [[], [], [], [], [], [], [], []]
 for i in range(len(a)):
 c = 0
 for j in range(len(a[i])):
 if a[i][j] == "1":
 c += 1
 b[c].append(a[i])
 return bdef compare(a, b):
 c = 0
 s = ""
 for i in range(len(a)):
 if a[i] == b[i]:
 c += 1
 s = s + a[i]
 else:
 s = s + "_"
 if c == len(a) - 1:
 return "t", s
 else:
 return "f", s
def mul(d):
 c = []
 for i in range(len(d)):
 d[i][0].sort()
 for i in range(len(d) - 1):
 a = d[i]
 if a not in d[i + 1::]:
 c.append(a)
 c.append(d[len(d) - 1])
 return c
def numm(n, d):
 e = []
 for i in range(len(n)):
 a = n[i]
 c = 0
 k = 0
 for j in range(len(d)):
 if a in d[j][0]:
 c += 1
 k = j
 if c == 1:
 e.append(k)
 return e
def reducedprime(dbp, e, nob):
 l3 = []
 l4 = []
 l5 = []
 k = []
 for i in range(len(dbp)):
 if i not in e:
 l3.append(i)
 l5.append([[], dbp[i][1]])
 k.append(dbp[i][1])
 else:
 l4 = l4 + dbp[i][0]
 #print("k is", k)
 rp = [] p = 0
 for i in l3:
 a = dbp[i][0]
 for j in range(len(a)):
 if a[j] not in l4:
 l5[p][0].append(a[j])
 p += 1
 print(l5)
 l6 = []
 for i in range(len(l5)):
 l6 = l6 + l5[i][0]
 l6 = set(l6)
 l6 = list(l6)
 l6.sort()
 #print("l6 is", l6)
 a = []
 for i in range(len(l5)):
 a.append(l5[i][0])
 c = l6
 yes = []
 for j in range(1, len(a) + 1):
 comb = combinations(a, j)
 for i in list(comb):
 aa = []
 i = list(i)
 for k in range(j):
 aa = aa + i[k]
 aa = set(aa)
 aa = list(aa)
 aa.sort()
 if aa == c:
 yes.append(i)
break
 yes1 = []
 for i in range(len(yes)):
 yes1.append(len(yes[i]))
 rp = []
 if len(yes1)!=0:
 min_value = min(yes1)
 min_index = yes1.index(min_value)
 aa = yes[min_index]
 #print(aa)
 yes2 = []
 yes3 = []
 for i in range(len(l5)):
 yes2.append(l5[i][0])
 yes3.append(l5[i][1])
 for i in range(len(aa)):
 a = yes2.index(aa[i])
 rp.append(yes3[a])
 return rp
# creating a number listgrp = grp0 + grp1 + grp2 + grp3 + grp4 + grp5 + grp6 + grp7 + grp8
print("grp is", grp)
l = []
gg = []
bb = [[], [], [], [], [], [], [], []]
db = []
dbp = []
gg.append(G0)
gg.append(G1)
gg.append(G2)
gg.append(G3)
gg.append(G4)
gg.append(G5)
gg.append(G6)
gg.append(G7)
gg.append(G8)
# print("gg is ",gg)
check = []
num = []
for i in range(len(gg) - 1):
 for j in range(len(gg[i])):
 c = 0
 a = gg[i][j]
 kk = ""
 for k in range(len(gg[i + 1])):
 b = gg[i + 1][k]
 st = compare(a, b)
 kk = st[1]
 if st[0] == "t":
 c = 1
 num.append([int(a, 2), int(b, 2)])
 bb[i].append(st[1])
 db.append([[int(a, 2), int(b, 2)], st[1]])
 check.append(a)
check.append(b)
 if c != 1 and a not in check:
 l.append(a)
 dbp.append([[int(a, 2)], a])
 num.append(int(a, 2))
n = len(gg) - 1
for i in range(len(gg[n])):
 if gg[n][i] not in check:
 l.append(gg[n][i])
 dbp.append([[int(gg[n][i], 2)], gg[n][i]])
def ind(a, d):
 for i in range(len(d)):
 if a in d[i]:
 return d[i][0]
 break
# step b
kkk = []kkk.append(bb)
db2=[]
db2.append(db)
check1 = []
p = 0
while True:
 y=p+1
 db2.append([])
 dd=db2[p]
 # print(p)
 che = kkk[p]
 # print("kkk is",kkk)
 ff = []
 # print(che,"p is",p)
 for i in range(len(che) - 1):
 for j in range(len(che[i])):
 c = 0
 a = che[i][j]
 for k in range(len(che[i + 1])):
 b = che[i + 1][k]
st = compare(a, b)
 if st[0] == "t":
 c = 1
ff.append(st[1])
db2[y].append([ind(a, dd) + ind(b, dd), st[1]])
 check1.append(a)
 check1.append(b)
 if c != 1 and a not in check1:
 l.append(a)
 dbp.append([ind(a, dd), a])
 n = len(che) - 1
 for i in range(len(che[n])):
 if che[n][i] not in check1:
 l.append(che[n][i])
 db2[y].append(ind(che[n][i], dd), che[n][i])
 ff = set(ff)
 ff = list(ff)
 if ff == []:
 break
 rr = convert(ff)
 # print("ff is",ff)
 kkk.append(rr)
 p += 1
dbp.extend(db2[len(db2)-1])
dbp=mul(dbp)
l = set(l)
l = list(l)
print("the prime implicans are ", l)
e=numm(grp,dbp)
e=set(e)
e=list(e)
l2=[]for i in e:
 l2.append(dbp[i][1])
l3=[]
for i in range(len(dbp)):
 if i not in e:
 l3.append(i)
def disp(l2):
 v = ["X7", "X6", "X5", "X4", "X3", "X2", "X1", "X0"]
 p = ["x̄7", "x̄6", "x̄5", "x̄4", "x̄3", "x̄2", "x̄1", "x̄0"]
 ep = []
 nn = 8 - nob
 for k in range(len(l2)):
 a = l2[k]
 s = ""
 for i in range(len(a)):
 if a[i] != "_":
 if a[i] == "0":
 s = s + p[nn + i]
 else:
 s = s + v[nn + i]
 ep.append(s)
 return ep
print("essential prime implicants are", end=" ")
ep=disp(l2)
if len(ep)!=0:
 for i in range(len(ep) - 1):
 print(ep[i], " + ", end="")
 if len(ep)-1==0:
 print(ep[0])
 else:
 print(ep[i + 1])
rp=reducedprime(dbp, e,nob)
ee=disp(rp)
if len(ee)!=0:
 print("Reduced prime implicants are")
 for i in range(len(ee) - 1):
 print(ee[i], " + ", end="")
 if len(ee)-1==0:
 print(ee[0])
 else:
 print(ee[i + 1])
ep.extend(ee)
print("THE Minimal Boolean Expression is")
if len(ep)!=0:
 for i in range(len(ep) - 1):
 print(ep[i], " + ", end="")
 if len(ep)-1==0:
 print(ep[0])
 else:
 print(ep[i + 1])
if ep[0]=="":
 print("1")
