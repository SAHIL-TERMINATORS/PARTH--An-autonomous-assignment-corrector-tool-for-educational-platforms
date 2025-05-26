from sentence_transformers import SentenceTransformer, util
from PyPDF2 import PdfReader
# Load a pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Single question and its corresponding paragraph answer
question = 'What is climate change and its effects on the environment?'

answer_paragraph = PdfReader("C:/Users/sahil/Downloads/DATABASE MANAGEMENT SYSTEMS.pdf")
page =answer_paragraph.pages[0]
a=page.extract_text()



# Compute embeddings for the question and answer paragraph
question_embedding = model.encode([question], convert_to_tensor=True)
answer_embedding = model.encode([answer_paragraph], convert_to_tensor=True)

# Compute cosine similarity between the question and answer embeddings
cosine_similarity = util.cos_sim(question_embedding, answer_embedding)

# Output similarity score
print("Question: {}\nAnswer Paragraph: {}\nSimilarity Score: {:.4f}".format(question, a, cosine_similarity[0][0]))
