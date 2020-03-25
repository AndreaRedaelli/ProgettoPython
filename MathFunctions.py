#region Import
#endregion

#function: fibonacci
def fib(n):    
    a, b = 0, 1
    while b < n:
        print (b),
        a, b = b, a+b

#function: lowest
def lowest(t):
    a = t[0];
    for i in t:
        if(a > i):
            a = i;
    print("The Lowest is " + str(a))

#function:heighest
def heighest(t):
    a = t[0];
    for i in t:
        if(a < i):
            a = i;
    print("The Heighest is " + str(a))

#function fattoriale
def fattoriale(n):
    if(n == 0 | n==1):
        return 1;
    else:
        return n * fattoriale(n-1);
