import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
   
# Input text - to summarize 
text = """  If you're certain that you're using the correct import statement and the package is correctly installed, but you're still encountering this error, there might be an issue with the package itself. In that case, you can try reaching out to the package maintainers for support or checking the package's issue tracker on its repository (if available) for solutions.

If you can provide more context about how you're using the gramform package and the specific import statement you're using, I might be able to offer more targeted assistance.




User

TypeError: 'module' object is not callable
ChatGPT
The error message "TypeError: 'module' object is not callable" typically occurs when you're trying to use a module as if it were a function or a callable object. This happens when you accidentally treat a module itself as something that can be called with parentheses, like a function.

Here are some common scenarios that might lead to this error:

Calling a Module Directly: If you have code that looks like module_name(), this would result in the error. Modules can't be called directly; only functions, classes, and certain callable objects can be invoked using parentheses.

Misusing Function or Class Names: Double-check if you're using the correct function or class name. If you're trying to call a function or instantiate a class, make sure you've spelled the name correctly and that it's actually a function or class defined within the module.

Incorrect Import: If you're importing a module and trying to call it like a function, it might indicate a misunderstanding of how the module should be used.

To resolve this error, review the part of your code that's triggering the error and ensure you're using functions, classes, or callable objects correctly. If you can provide the specific code snippet that's causing the error, I can provide more targeted guidance on how to correct it.





 """
   
# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)
   
# Creating a frequency table to keep the 
# score of each word
   
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1
   
# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()
   
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq
   
   
   
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
   
# Average value of a sentence from the original text
   
average = int(sumValues / len(sentenceValue))
   
# Storing sentences into our summary.
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
print(summary)
