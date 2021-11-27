import os
import shutil
import glob 

if os.path.exists("target_file"):
    print("File already exists")
else:
    os.mkdir("target_file")
src="source_file"
source=os.listdir(src)
target="target_file"

for file in source:
    shutil.copy2(os.path.join(src,file),target)