from PyPDF2 import*
pdf=PdfFileReader("Ampi vaccination certificate.pdf") #getting pdf file to encrypt
pdfwriter=PdfFileWriter() #making a copy file of original file for encrypting

for page_num in range(pdf.numPages): #using loop we will add pages from pdf to pdfwriter
    pdfwriter.addPage(pdf.getPage(page_num)) #from pdf, we are getting one page(page_num) in every iteration.
    #after getting that page, we will add that page to the pdfwriter (addPage and getPage are methods in this module)
password="haiyehai" #assigning password
pdfwriter.encrypt(password) #encrypt method for encrypting this newly copied pdf file

with open("certificate1.pdf","wb") as f: #creating new pdf file named (newfile.pdf), wb because we are writing this file
    # in binary form and we donot want to change the orogonal content of pdf file
    pdfwriter.write(f)

f.close