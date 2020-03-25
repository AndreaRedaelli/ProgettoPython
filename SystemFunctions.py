#region Import
import platform
#endregion

#function sysInfo
def sysInfo():
    print(str(platform.architecture()));
    print(str(platform.processor()));
    print(str(platform.system()));
    print(str(platform.uname()));
