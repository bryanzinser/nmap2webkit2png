import subprocess, time, os, sys

iplist = []

def runwebkit2png(a):
    i = 1
    p = {}

    for item in a:
	    
        j = 1
        arg = ['python', 'webkit2png.py', '-D', 'img/']
        ip = 'http://' + item
        arg.append(ip)
        
        if i < 6:
            p[i] = subprocess.Popen(arg)
            i += 1
        else:
            time.sleep(6)
            while j < 6:
                p[j].terminate()
                j += 1
            i = 1
            p = {}
            
def getformatedlist():
    i = 1
    while i <= 9:
        arg = "log/linode-scan-%d" % i
        indata = open(arg)
        for line in indata:
            if "open" in line:            
                line = line.split(' ')
                iplist.append(line[1].rstrip())
        i += 1
        indata.close()
    return iplist



formatedlist = getformatedlist()
runwebkit2png(formatedlist)
