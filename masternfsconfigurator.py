import os

sf = open("workers","r")
sip = sf.read().replace("-","")
sf.close()

sip2 = sip.split('\n')
sip2.remove('')
sip2.remove('')
sip2.remove('')

os.system("apt update")
os.system("apt -y install nfs-kernel-server")

os.system("mkdir /root/shared -p")
os.system("chown nobody:nogroup /root/shared")
os.system("chmod 777 /root/shared")

newconfig = "/root/shared" + " " + " " + " "
for i in range(len(sip2)):
    newconfig = newconfig + "  {}\(rw,sync,no_subtree_check,no_root_squash\)".format(sip2[i])
    os.system("ufw allow from {} to any port nfs".format(sip2[i]))

os.system("echo {} >> /etc/exports".format(newconfig))
os.system("exportfs -a")
os.system("systemctl restart nfs-kernel-server")

#os.system("ufw allow ssh")
#os.system("ufw --force enable")
