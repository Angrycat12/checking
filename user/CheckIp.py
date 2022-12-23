import os
import subprocess 



def GettingIp ():
    
    subprocess.run(["netstat","-n",">logfile.txt"],stdout=subprocess.DEVNULL)
    pass

def ip ():
    
    IpOutput = []
    IpInputls = []
    IpInput = []
    
    with open('logfile.txt') as f:
        IpInput = [line.rstrip('\n') for line in f] #делим по строкам
    
    for line in IpInput: # делим по пробелам
        if not line.strip():
            print('error 20')
            continue
        IpInputls.append(line.lstrip())
    IpInput = IpInputls
    
    ##print(IpInput)
    
    for iteration in range(len(IpInput)):
        if iteration > 1:
            IpInputls = IpInput[iteration].split() 
            for iterations in range(len(IpInputls)):
                if iterations == 2:
                    IpOutput.append(IpInputls[iterations])
    
    ##print(IpOutput)
                
    return IpOutput

def CheckIp ():
    
    GettingIp()
    
    IpCheck = ip()
    BlockedIp = 0
    
    #for ip in IpCheck:
        #if ip in BlockedIp:
            
    
    return IpCheck
 
if __name__ == "__main__":
    
    ips = CheckIp()
    print(ips)
