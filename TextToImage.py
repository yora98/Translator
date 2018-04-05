import os
from Converter import Converter

class TextToImage:
    folder_path=""
    list = []
    list_txt = []
    total_content = {}
    word=""
    finding=[]
    def __init__(self,f_path,w):
        self.folder_path=f_path
        self.word=w

    def textDict(self):

        items=os.listdir(self.folder_path)


        for name in items:
            if(name.endswith(".png") or name.endswith(".jpg") or name.endswith(".jpeg")):
                self.list.append(name)
            else:
                self.list_txt.append(name)

        #print(list)
        #print(list_txt)

        for file in self.list:
            temp=file+".txt"
            if temp not in self.list_txt:
                content=Converter(file,self.folder_path).execute()
                self.total_content[file]=content
                #print("hi")
            else:

                 s=file+".txt"

                 os.chdir(self.folder_path)
                 self.total_content[file] = open(s,'r',encoding="utf-8").read()
        #print(len(self.total_content))

    def search(self):

        self.finding=[]

        for key,value in self.total_content.items():


            if self.word in value:
                self.finding.append(key)
        print(self.finding)
        return self.finding


#obj1=TextToImage("/home/yogesh/Hackathon CSI-9 September 2017/ProblemStatement_1/Images_OCR","the")

#obj1.textDict()
#print(obj1.search())