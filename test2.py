import os
import shutil
import sys
from time import sleep

if os.path.exists("targetper"):
    print("file aready present")
else:
    os.mkdir("targetper")

src="source_file"
targe="targetper"
contain=os.listdir(src)
def perctage(contain,src,targe):
    
    for i in range(21):
        sys.stdout.write('\r')
        for file in contain:
            shutil.copy2(os.path.join(src,file),targe)
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
    sleep(5.42)
        
perctage(contain,src,targe)
    