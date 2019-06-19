import os

mf = open("master","r")
mip = mf.read().strip()
mf.close()

os.system("apt update")
os.system("apt -y install nfs-common")

os.system("mkdir -p /root/shared")
print("directory created")
os.system("mount {}:/root/shared /root/shared".format(mip))
