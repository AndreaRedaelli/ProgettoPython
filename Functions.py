import time
import winsound
#functions: fibonacci
# scrive le serie di Fibonacci fino a n
def fib(n):    
    a, b = 0, 1
    while b < n:
        print (b),
        a, b = b, a+b

def acoustic_wait_signal(interval):
    while(True):
        winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
        time.sleep(int(interval))

def lowest(t):
    a = t[0];
    for i in t:
        if(a > i):
            a = i;
    print(a);

def heighest(t):
    a = t[0];
    for i in t:
        if(a < i):
            a = i;
    print(a);