#region import
import SystemFunctions
import MathFunctions
import GenericFunctions
import _thread
import time
#endregion

#region thread 
_thread.start_new_thread( GenericFunctions.acoustic_signal, (1,) )
#endregion
print("Hi !");

#region SysInfo
SystemFunctions.sysInfo();
#endregion

#region Fibonacci Function 
input_var = input("Please insert a value \n");
print("Fibonacci's sequence ")
MathFunctions.fib(int(input_var));
#endregion

#region Fattoriale Function
result = MathFunctions.fattoriale(int(input_var));
print("Fattoriale : " + str(result));
#endregion

#region Min/Hig/Histogram 
lista_numeri = [];
uscita = False;
while(uscita == False):
    num = input("Choos a number, -1 to quit \n");
    if(int(num) == -1):
        uscita = True
    else:
        lista_numeri.append(int(num));
print("List : ");
print(lista_numeri);
if(len(lista_numeri) > 0):
    MathFunctions.lowest(lista_numeri);
    MathFunctions.heighest(lista_numeri);
    GenericFunctions.histogram(lista_numeri);
#endregion
