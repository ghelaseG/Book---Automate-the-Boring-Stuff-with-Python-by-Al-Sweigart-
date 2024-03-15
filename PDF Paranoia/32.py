#python3!
#Using the os.walk() function from Chapter 10, write a script that will go through every PDF
#in a folder (and its subfolders) and encrypt the PDFs using a password provided on the command line
#Then, write a program that finds all encrypted PDFs in a folder (and its subfolders) and creates a
#decrypted copy of the PDF using a provided pass- word.

import os
import PyPDF2
import re
import pprint

os.chdir(r'/Users/georgeghelase/Desktop/pdf')
path = os.getcwd()

pdf_list = ['first.pdf', 'second.pdf', 'third.pdf']

for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith(('.pdf', '.PDF')):
            try:
                pdf = open(os.path.join(folder, file), 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf)
                pdf_reader.getPage(0)
            except PyPDF2.utils.PdfReadError:
                try:
                    pdf = open(os.path.join(folder, file), 'rb')
                    print(os.path.join(folder, file))
                    pdf_reader = PyPDF2.PdfFileReader(pdf)
                    pdf_reader.decrypt('#choose a password')
                    pdf_reader.getPage(0)
                    print('Decrypting %s...' % file)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for page_num in range(0, pdf_reader.numPages):
                        page_obj = pdf_reader.getPage(page_num)
                        pdf_writer.addPage(page_obj)
                    new_name = re.sub('_encrypted', '_decrypted', file)
                    new_pdf = open(os.path.join(folder, new_name), 'wb')
                    pdf_writer.write(new_pdf)
                    pdf.close()
                    new_pdf.close()
                    pdf_list.append(file)
                except PyPDF2.utils.PdfReadError:
                    print('Could not decrypt %s' % file)

print('Successfully decrypted the following:')
pprint.pprint(pdf_list)
