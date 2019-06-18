import os

sf = open("workers","r")
sip = sf.read().replace("-","")
sf.close()

sip2 = sip.split('\n')
sip2.remove('')
sip2.remove('')
sip2.remove('')
newconfig = "/var/nfs/general" + " " + " " + " "
for i in range(len(sip2)):
    newconfig = newconfig + "  {}\(rw,sync,no_subtre_check\)".format(sip2[i])

os.system("echo %s >> /etc/exports" %newconfig)
