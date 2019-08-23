# Karatsuba Multiplication
from math import ceil

def pad(str, n, side="left"):
    if side == "left":
        for _ in range(0,n):
            str = "0"+str
    else:
        for _ in range(0,n):
            str = str+"0"
    return str

def string_operate(s, r, op="add"):

    lens = len(s)
    lenr = len(r)
    if lens > lenr:
        # Pad r with zeros to the left
        r = pad(r, lens-lenr)
    elif lens < lenr:
        # Pad s with zeros to the left
        s = pad(s, lenr-lens)

    carry = 0
    result = ""
    if op=="add":
        for i in range(max(lens, lenr)-1, -1, -1):
            partial = str(int(s[i])+int(r[i])+carry)
            if len(partial) == 2:
                carry = int(partial[0])
            else:
                carry = 0
            result = partial[-1] + result
    elif op=="subtract":
        for i in range(max(lens, lenr)-1, -1, -1):
            if int(s[i])-carry >= int(r[i]):
                partial = str(int(s[i])-carry-int(r[i]))
                carry = 0
            else:
                partial = str(10+(int(s[i])-carry)-int(r[i]))
                carry = 1
            result = partial[-1] + result
    else:
        raise("Error: wrong string operation!")

    if carry != 0:
        result = str(carry)+result
    return result

def recursive_multiplication(x,y):

    if len(x) == 1 and len(y) == 1:
        return str(int(x)*int(y))
    else:
        n = len(x)
        if n > len(y):
            # Pad y with zeros[n-len(y)]
            y = pad(y, n-len(y))
        else:
            # Pad x with zeros
            x = pad(x, len(y)-n)
            n = len(x)

        half = ceil(n/2)

        # Procedure:
        # 1. Split each n-digit number into 2 n/2-digit numbers

        a = x[0:half]
        b = x[half:]

        c = y[0:half]
        d = y[half:]

        # 2. Recursively compute a*c
        
        ac = recursive_multiplication(a, c)

        # 3. Recursively compute b*d
        
        bd = recursive_multiplication(b, d)

        # 4. Recursively compute (a+b)*(c+d) = ac + (ad + bc) + bd

        aplusb = string_operate(a, b, op="add")
        cplusd = string_operate(c, d, op="add")

        bigproduct = recursive_multiplication(aplusb, cplusd)
        
        # 5. Gauss' trick: (ad+bc) = (ad+bc) - a*c - b*d

        acplusbd = string_operate(ac, bd, op="add")
        middleproduct = string_operate(bigproduct, acplusbd, op="subtract")

        # Finally:
        # Pad middle product: 10**(n-half)*middleproduct
        middleproduct_padded = pad(middleproduct, n-half, side="right")
        partialproduct = string_operate(middleproduct_padded, bd, op="add")
        
        # Pad ac: (10**n)*ac
        padded_ac = pad(ac, n-n%2, side="right")
        finalproduct = string_operate(padded_ac, partialproduct, op="add")

        return finalproduct

if __name__ == "__main__":
    pi  = "3141592653589793238462643383279502884197169399375105820974944592"
    exp = "2718281828459045235360287471352662497757247093699959574966967627"

    result = recursive_multiplication(pi, exp)

    if result == "8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184":
        print("Ok!")
    else:
        print("Error")
