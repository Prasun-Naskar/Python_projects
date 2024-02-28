import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download('stopwords')
#nltk.download('punkt')

text = "Hi, My name is Aman Kharwal, I am here to guide you to your journey in Machine Learning for free."
tokens = word_tokenize(text)
tokenization = [word for word in tokens if not word in stopwords.words('english')]
print(tokens)
print(tokenization)