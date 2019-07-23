import sys
import os
import platform
import subprocess

plat = platform.system()
scriptDir = sys.path[0]
firewalls = os.path.join(scriptDir, 'firewalls.txt')
firewallsFile = open(firewalls, "r")
lines = firewallsFile.readlines()
def firewalls():
    for line in lines:
        line = line.strip( )
        if plat == "Windows":
            response = os.system("ping -n 1 " + line )
       
        if response == 0:
            print(line, 'is up!')
        else:
            print(line, 'is down!')
            

        
firewallsFile.close()

if __name__ == "__main__":
    firewalls()
    
