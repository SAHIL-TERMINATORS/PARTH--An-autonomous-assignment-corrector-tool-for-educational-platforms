import Levenshtein
import PyPDF2

chatgpt_responses =input("enter the chatgpt response")
pdf1_path = input("Enter the path of pdf1: ")

# Read and tokenize PDF1
with open(pdf1_path, 'rb') as file:
    pdf_read = PyPDF2.PdfReader(file)
    extracted_token1 = []

    for page_number in range(len(pdf_read)):
        page = pdf_read.pages[page_number]
        submitted_text = page.extract_text()


def check_similarity(submitted_text):
    lowest_distance = float("inf")
    most_similar_response = None

    for response in chatgpt_responses:
        distance = Levenshtein.distance(submitted_text.lower(), response.lower())
        
        if distance < lowest_distance:
            lowest_distance = distance
            most_similar_response = response

    # You can set a threshold for similarity distance to make a decision
    threshold = 10
    if lowest_distance <= threshold:
        return f"The assignment text is similar to: '{most_similar_response}'"
    else:
        return "The assignment text is not significantly similar to ChatGPT's responses."

response=print("chatgpt's response is:",check_similarity(submitted_text))
