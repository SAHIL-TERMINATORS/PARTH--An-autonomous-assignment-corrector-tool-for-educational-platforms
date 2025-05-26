import PyPDF2
import nltk
nltk.data.path.append('C:\\Program Files\\Python311\\lib\\nltk_data')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

pdf_path = input("Enter the path of pdf: ")
maxm_len=int(input("enter the word limit maxm"))
minm_len=int(input("enter the word limit minm"))
with open(pdf_path, 'rb') as file:
    pdf_read = PyPDF2.PdfReader(file)
    extracted_token1 = []

    for page_number in range(len(pdf_read.pages)):
        page = pdf_read.pages[page_number]
        text1 = page.extract_text()
        token1 = word_tokenize(text1)
        extracted_token1.extend(token1)

    unique_tokens1 = (extracted_token1)
Count =len(extracted_token1)
if( Count<minm_len):
    print(" you have to write more")
if(Count>minm_len and Count<=maxm_len):
    print("good but not sufficient")
else:
    print("word limit meets with instructions")
