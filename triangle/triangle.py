def TestInput(a):
    if (isinstance(a, str)):
        return False
    elif (a > (pow(2, 32) - 1)):
        return False
    else:
        return True

def ConvertType(a):
    try:
        return float(a)
    except ValueError:
        return "string"

def detect_triangle(a,b,c):
    a = ConvertType(a)
    b = ConvertType(b)
    c = ConvertType(c)
    if (TestInput(a) == False or TestInput(b) == False or TestInput(c) == False):
        return "Input invalid!"
    elif ((a+b)>c and (a+c)>b and (b+c)>a and (a>0) and (b>0) and (c>0)):
       if(a==b)and (b==c):
           return "Tam giac deu"
       elif((a*b+b*b==c*c)and(a==b))or((a*a+c*c==b*b)and(a==c))or((c*c+b*b==a*a)and(c==b)):
           return "Tam giac vuong can"
       elif(a==b)or(b==c)or(a==c):
           return "Tam giac can"
       elif((a*a==b*b+c*c)or(b*b==a*a+c*c)or(c*c==a*a+b*b)):
           return "Tam giac vuong"
       else:
           return "Tam giac thuong"
    else:
       return "Input invalid!"
