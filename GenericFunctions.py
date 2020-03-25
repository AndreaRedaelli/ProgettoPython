#region Import
import winsound
import time
#endregion

#function histrogram
def histogram(t):
    for i in t:
        print("Number " + str(i));
        s = "";
        for x in range(0,i):
            s = s + ("X");
        print(s + "\n");

#function acoustic_signal
def acoustic_signal(interval):
    while(True):
        winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
        time.sleep(int(interval))
