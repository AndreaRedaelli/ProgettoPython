import Functions


import _thread
import time
#region thread 
_thread.start_new_thread( Functions.acoustic_wait_signal, (1,) )
#end
print("Ciao, andiamo a giocare un pochino con python");

input_var = input("inserisci un valore qualsiasi \n");

Functions.fib(int(input_var));
lista_numeri = [];

uscita = False;
while(uscita == False):
    num = input("inserisci un numero della lista, -1 per terminare \n");
    if(int(num) == -1):
        uscita = True
    else:
        lista_numeri.append(int(num));
print(lista_numeri);
Functions.lowest(lista_numeri);