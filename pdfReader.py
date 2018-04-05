import PyPDF2
import pdftotext

class Pdfread(object):
   path=""
   extracted_text=""
   file_name=""

   def __init__(self,path1,file):
        self.path=path1
        self.file_name=file
        print(path1)

   def extract(self):


       # Load your PDF
       with open(self.path, "rb") as f:
           pdf = pdftotext.PDF(f)

       # How many pages?
       # print(len(pdf))

       # Iterate over all the pages

       # Read some individual pages


       # Read all the text into one string
       a = "\n\n".join(pdf)
       print(a)
       return a