import os

class Converter(object):
    file_name=""
    img_path=""
    def __init__(self,file_nam,path):
        self.file_name=file_nam
        self.img_path=path


    def execute(self):
        os.chdir(self.img_path)
        command="tesseract "+ self.file_name+" "+self.file_name+" -l eng"
        #os.system("tesseract "+ self.file_name+" "+self.file_name+" -l eng")
        os.system(command)
        path=self.img_path+"/"+self.file_name+".txt"
        file_obj=open(path,'r',encoding="utf-8")
        img_text=file_obj.read()
        return img_text