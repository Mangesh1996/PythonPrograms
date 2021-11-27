import os
import sys
from time import sleep
import shutil
import glob

if os.path.exists("only_jpeg"):
    print("FIle already exists")
else:
    os.mkdir("only_jpeg")
if os.path.exists("only_pdf"):
    print("FIle already exists")
else:
    os.mkdir("only_pdf")

src="source_file"
contain=os.listdir(src)
target="only_jpeg"
target1="only_pdf"

def Copyonlyjpeg(src,targer):
    for i in range(21):
        sys.stdout.write("\r")
        for filenam in glob.glob(os.path.join(src,"*.jpg")):
            shutil.copy(filenam,targer)
        sys.stdout.write("[%-20s]%d%%" %( "="* i,5*i) )
    sys.stdout.flush()
    sleep(0.2)
    print("\n")
    print("All Jpeg File copy to designation directory ")
    print("\n")

def Copyonlypdf(src,target):
    sleep(1.0)
    for i in range(21):
        sys.stdout.write("\r")
        for file in glob.glob(os.path.join(src,"*.pdf")):
            shutil.copy(file,target)
        sys.stdout.write("[%-20s] %d%%" %("="* i,5*i))
    sys.stdout.flush()
    sleep(0.2)
    print("\n")
    print("All the Pdf file copy to pdf directory")
Copyonlyjpeg(src,target)
Copyonlypdf(src,target1)
    