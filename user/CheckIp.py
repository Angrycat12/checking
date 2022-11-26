import os
import sys


def ip ():
    IpInput = str(os.system('netstat -n'))
    IpOutput = []
    iteration = 1
    IpInputls = []
    print(IpInput)
    
    for line in IpInput.split("\n"):
        if not line.strip():
            print('gg')
            continue
        IpInputls.append(line.lstrip())
    IpInput = IpInputls
    
    print(IpInput)
    
    for iteration in range(len(IpInput)):
        if iteration % 4 == 0:
            IpOutput = IpInput[iteration]
    return IpOutput
ips = ip()
print(ips)
