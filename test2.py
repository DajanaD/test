file*
import sys
import os
import codecs
from PyPDF2 import PdfFileReader

# with open ('new.pdf','r+') as test_file:

#    read_file =test_file.read().replace("подшипника", "підшипника")
   
   
# with open ('new.pdf', 'w') as test_file:
#     test_file.write(read_file)
 
with codecs.open('test5.pdf', 'r', encoding='latin-1') as test_file:
    
    lines =test_file.readlines()
    print(lines)