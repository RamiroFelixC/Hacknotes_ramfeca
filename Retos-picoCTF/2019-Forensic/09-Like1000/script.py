import tarfile

for i in range(1000,0,-1):
        arch="{}.tar".format(i)
        tar=tarfile.open(arch)
        tar.extractall()
        tar.close()
        
