import os

mf = open("master","r")
mip = mf.read().strip()
mf.close()

os.system("apt -y install nfs-common")

os.system("mkdir -p /nfs/general")
os.system("mount {}:/var/nfs/general /nfs/general".format(mip))
