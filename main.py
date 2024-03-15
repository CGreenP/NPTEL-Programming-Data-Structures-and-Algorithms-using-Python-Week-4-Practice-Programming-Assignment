def orangecap(dict1):
    dict2 = {}
    for k1 in dict1:
        for k2 in dict1[k1]:
            dict2[k2] = dict2.get(k2, 0) + dict1[k1][k2]
    player = max(dict2, key=dict2.get)
    return (player, dict2[player])

def addpoly(p1,p2):
        for i in range(len(p1)):
            for item in p2:
                if p1[i][1] == item[1]:
                    p1[i] = ((p1[i][0] + item[0]),p1[i][1])
                    p2.remove(item)
        p3 = p1 + p2
        for item in (p3):
            if item[0] == 0:
                p3.remove(item)
        return (sorted(p3))

def takeSecond(elem):
    return (elem[1])
def multpoly(p1,p2):
    res=[]
    lenp1=len(p1)
    lenp2=len(p2)
    for i in range(lenp1):
        for j in range (lenp2):
            p=((p1[i][0]*p2[j][0]),(p1[i][1]+p2[j][1]))
            res.append(p)
    return (cancel(res))
def cancel(l):
    a=[]
    res=[]
    ret=[]
    for i in l:
        l3=i[1]
        a.append(l3)
    b=(list(set(a)))
    for y in b:
        sum=0
        for z in l:
            if (y==z[1]):
                sum=sum+z[0]
        res.append(sum)
    for j in range (len(b)):
        if (res[j]==0):
            continue
        else:
            to = (res[j],b[j])
            ret.append(to)
    return (sorted(ret,key=takeSecond,reverse=True))
import ast

def todict(inp):
    inp = ast.literal_eval(inp)
    return (inp)

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "orangecap":
   arg = todict(farg)
   print(orangecap(arg))
elif fname == "addpoly":
   (arg1,arg2) = topairoflists(farg)
   print(addpoly(arg1,arg2))
elif fname == "multpoly":
   (arg1,arg2) = topairoflists(farg)
   print(multpoly(arg1,arg2))
else:
   print("Function", fname, "unknown")
  

