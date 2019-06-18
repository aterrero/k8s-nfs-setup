import os

sf = open("workers","r")
sip = sf.read().replace("-","")
sf.close()

sip2 = sip.split('\n')
sip2.remove('')
sip2.remove('')
sip2.remove('')

os.system(ufw enable)
os.system(ufw allow ssh)

os.system("mkdir /var/nfs/general -p")
os.system("chown nobody:nogroup /var/nfs/general")

newconfig = "/var/nfs/general" + " " + " " + " "
for i in range(len(sip2)):
    newconfig = newconfig + "  {}\(rw,sync,no_subtre_check\)".format(sip2[i])
    os.system("ufw allow from {} to any port nfs".format(sip2[i]))

os.system("echo {} >> /etc/exports".format(newconfig))
os.system("systemctl restart nfs-kernel-server")
