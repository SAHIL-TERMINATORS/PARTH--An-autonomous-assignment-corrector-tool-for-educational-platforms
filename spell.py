from TextBlob import TextBlob

def spellcheck(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return corrected_text

input_text = "Helo, how are yu?"
corrected_text = spellcheck(input_text)
print("Original Text:", input_text)
print("Corrected Text:", corrected_text)
