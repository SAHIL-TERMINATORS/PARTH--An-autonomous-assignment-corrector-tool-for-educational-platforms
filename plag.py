import pytesseract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from difflib import SequenceMatcher


def extract_tokens_from_image1(image_path1):
    image_text = pytesseract.image_to_string(image_path1)
    return  image_text

def extract_tokens_from_image2(image_path2):
    image_text = pytesseract.image_to_string(image_path2)
    return  image_text

tokens_from_image1 = extract_tokens_from_image1(image_path1)
tokens_from_image2 = extract_tokens_from_image2(image_path2)

image_path1 = input("Enter the path of the image: ")
image_path2 = input("Enter the path of the image: ")

similarity=SequeneMatcher(None,image_path1,image_path2).ratio()
print(f"the contents are",(similarity*100)%"common")
if(similarity<50):
    print(" both contents are plag -free")
else:
    print(" contents are not plag _free")



