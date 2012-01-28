import subprocess, time, os, sys, math

iplist = []

def runwebkit2png(a):
    awesome = 1
    p = {}
    for item in a:
        arg = ['python', 'webkit2png.py', '-D', 'img/']
        ip = 'http://' + item
        arg.append(ip)
        if awesome < 6:
            p[awesome] = subprocess.Popen(arg)
            awesome += 1
        else:
            time.sleep(6)
            p[1].terminate()
            p[2].terminate()
            p[3].terminate()
            p[4].terminate()
            p[5].terminate()
            awesome = 1
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



dude = getformatedlist()
runwebkit2png(dude)
