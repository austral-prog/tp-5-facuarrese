def roots(a, b, c):
    from math import sqrt
    vdr=(b**2-4*a*c)
    if vdr<0:
        return None
    else:
        vr=sqrt(vdr)
        pr = (b - (vr)/ (2 * a))
        sr = (b + (vr) / (2 * a))
    if  pr==sr:
        return (pr)
    else:
        return(pr,sr)


def to_string(a, b, c):
    if a-int(a)==0:
        a=int(a)
    if b-int(b)==0:
        b=int(b)
    if c-int(c)==0:
        c=int(c)

    a=str(a)
    b=str(b)
    c=str(c)
    if "-" in b:
        v=""
    else:
        v="+"
    if "-" in c:
        w = ""
    else:
        w = "+"
    print(f"{a}x²{v+str(b)+w+str(c)}")

def value_y(a,b,c,x):
    y=(a*(x**2)+b*x+c)
    return y

a=float(input("a "))
b=float(input("b "))
c=float(input("c "))
x=float(input("x "))

def derivation(a, b, c):
    pa= 2*a*'x'+b

(to_string(a,b,c))
print(value_y(a,b,c,x))
print(roots(a,b,c))
