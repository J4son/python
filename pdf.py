import os,re,sys,glob
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser, PDFDocument, PDFNoOutlines
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTChar, LTPage

list_fichier = []
chemin = "/Users/brur/Downloads/"
for (root,files,dirs,) in os.walk(chemin):
        for name in dirs:
               fichier = ''.join((root,"/",name))
               list_fichier.append(fichier)
               list_fichier = glob.glob(str(list_fichier)+"*.pdf")
               
        #for name in files:
         #       print '/'.join((root,str(dirs)))




#list_fichier = glob.glob(chemin+"*.pdf")
fichier = os.listdir(chemin)
tableau = []

for fic in fichier:
        if os.path.isdir(chemin+fic):
                tableau = chemin + fic + "/"
        else:
                list_fichier = glob.glob(chemin+"*.pdf")
                
                  
print "Veuillez entrer le terme recherche:" 
recherche =  raw_input()

for files in list_fichier:
        str2 = files
        fichier = open(str(files),"rb")
        parser = PDFParser(fichier)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize("")
        try:
                outline = doc.get_outlines()
                laparams = LAParams()
                resourcemgr = PDFResourceManager()
                device = PDFPageAggregator(resourcemgr, laparams=laparams)
                interpreter = PDFPageInterpreter(resourcemgr, device)
                for (level,title,dest,a,se) in outline:
                        strings2 = re.findall(recherche,title,re.IGNORECASE)
                        if strings2:
                                print "Fichier :",  str2, "\t" ,"Chapitre: ",title
                                       
                 
                
        except:
                pass

