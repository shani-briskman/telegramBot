import random
from os import listdir
from os.path import isfile, join
import views
import func
#from views import app
class Blesses:
    bless:str
    popular:int
    def __init__(self,bless):
        self.bless=bless
        self.popular=0

def create(kind):
    dict1={}
    myPath="C:\\Users\\shani\\Desktop\\blessProject\\"+kind
    onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
    for file in onlyfiles:
        currentFile = open(myPath+"\\"+file,'r',encoding='utf-8')
        bless = ""
        dict1[file[:-4]]=[]
        lines = currentFile.readlines()
        for line in lines:
            if not line.startswith("#"):
                bless += line  # [:-1]
            else:
                if (kind=="blesses"):
                 bless =Blesses(bless)
                dict1[file[:-4]].append(bless)
                bless = ""
    return dict1
blesses = create("blesses")
links = create("links")
emoji = create("emoji")

if __name__ == '__main__':

    views.app.run(port=8080)
    print(blesses)

