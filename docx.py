import os

class DocReader(object):
    file_name=""
    file_path=""
    def __init__(self,path,file_nam):
        self.file_name=file_nam
        self.file_path=path


    def extract(self):
        f = open(self.file_path, 'r')
        x=f.read()
        return x