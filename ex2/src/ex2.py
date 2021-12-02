import sys

def getUglyNumber(nth):
    i = 1

    found = 1
    while nth > found:
        i += 1
        if isUgly(i):
            found += 1
    return i

def isUgly(number):
    n = maxDivide(number, 2)
    n = maxDivide(n, 3)
    n = maxDivide(n, 5)
    return n == 1

def maxDivide(a, b):
    while a % b == 0:
        a = a / b 
    return a

if __name__=='__main__':
    if len(sys.argv) != 2:
        print("Indicate the nth ugly number to compute")
        sys.exit(1)
    
    nth = sys.argv[1]

    if not nth.isdigit():
        print("Indicate a number")
        sys.exit(1)
    
    n = getUglyNumber(int(nth))
    print(f"The {nth}th ugly number is {n}")