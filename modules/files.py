import os
from PIL import Image
import img2pdf
from PyPDF2 import PdfFileMerger
from zipfile import ZipFile
class files:
    
    def __init__(self):
        self.default_dir = os.getcwd()
        print ("Parsing downloaded files to pdf. This will take time. Please do not quit the program untill a success message is shown.")

    def getName(self):
        chapter = os.listdir(self.default_dir+"/files/")[0]
        ch = ""
        for i in chapter:
            try:
                float(i).is_integer()
                break
            except:
                ch += i
        self.chapter = ch

    def unzip(self, name): 
        with ZipFile(name, 'r') as zip:
            zip.extractall()
        #os.rename(name, self.default_dir+"/"+self.chapter)

    def processfiles(self):

        os.mkdir(self.chapter)
        files = os.listdir(self.default_dir+"/files/")
        for f in files:
            os.mkdir(f)
            self.processzip(f)


    def processzip(self,f):

        self.unzip(self.default_dir+"/files/"+f)
        files = os.listdir(self.default_dir)
        x = [a for a in files if (a.endswith(".jpeg") or a.endswith(".png") or a.endswith(".jpg"))]

        x = self.cleanFiles(x)

        for k in x:
            pdfPath = k+".pdf"
            image = Image.open(k)
            pdf_bytes = img2pdf.convert(image.filename)

            file = open(pdfPath, "wb")
            file.write(pdf_bytes)
            image.close()
            file.close()
            os.rename(k, self.default_dir+"/"+f+"/"+k)

        files = os.listdir(self.default_dir)

        x = [a for a in files if a.endswith(".pdf")]

        merger = PdfFileMerger()

        for pdf in x:
            merger.append(open(pdf, 'rb'))


        with open(f+".pdf", "wb") as fout:
            merger.write(fout)

        for pdf in x:
            os.remove(self.default_dir+"/"+pdf)

        os.rename(f+".pdf", self.default_dir+"/"+f+"/"+f+".pdf")


    def cleanFiles(self, lt):

        fl = lt[0]

        for i in fl:
            try:
                float(i).is_integer
                kt = fl.index(i)
                break
            except:
                pass
        #print (fl[kt:])
        for i in fl[kt:]:
            if i == "_":
                mt = len(fl[:kt])+1+fl[kt:].index(i)
                break

        kt = len(fl[:mt])
        #print (fl[:mt])

        lenlist = map(lambda x: len(x), lt)
        lenlist = list(lenlist)
        maxlen = max(lenlist)

        newFileArr = []

        for f in lt:
            if len(f) < maxlen:
                c = ""
                for j in range(maxlen-len(f)):
                    c+="0"
                t = f[:kt]+c+f[kt:]
                self.animeChapter = t
                os.rename(f,t)
                newFileArr.append(t)
            else:
                newFileArr.append(f)
        newFileArr.sort()
        return newFileArr

    def cleanImg(self):

        files = os.listdir(self.default_dir)
        for f in files:
            if f.startswith(self.chapter):
                files2 = os.listdir(self.default_dir+"/"+f)
                for f2 in files2:
                    if (f2.endswith(".jpeg") or f2.endswith(".png") or f2.endswith(".jpg")):
                        os.remove(self.default_dir+"/"+f+"/"+f2)

                    elif f2.endswith(".pdf"):
                        os.rename(self.default_dir+"/"+f+"/"+f2, self.default_dir+"/"+self.chapter+"/"+f2)


    def cleanZip(self):

        files = os.listdir(self.default_dir+"/files")
        for f in files:
            os.remove(self.default_dir+"/files/"+f)

    def cleanDir(self):

        files = os.listdir(self.default_dir)
        for f in files:
            if f.startswith(self.chapter):
                files2 = os.listdir(self.default_dir+"/"+f)
                if len(files2) == 0:
                    os.rmdir(f)
