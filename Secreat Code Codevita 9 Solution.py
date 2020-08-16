#i dont know. i missed some logic there. if anyone found tat implement it
def lststr(m):
    str1 = ""
    for ele in m:
        str1 += ele
    return str1
code = input()
N = int(input())
f = []
q = []
r= dict()
m = []

for i in range(N):
    x = []
    y = []
    lst = []
    p = str(input())
    q = p.split()
    for j in q:
        b = list(j)
        lst.append(b)
    x.append(lst[0])
    x = [item for items in x for item in items]
    y.append(lst[1])
    y = [item for items in y for item in items]
    wordbag = dict(zip(x, y))
    #print(wordbag)
    r.update(wordbag)

code = list(code)
r.keys()
for k in code:
    if k in r.keys():
        m.append(r[k])
        #print(m)
print(lststr(m))
















