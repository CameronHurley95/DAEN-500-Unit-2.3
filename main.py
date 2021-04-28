import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

nltk.download('stopwords')
textfile = open('NYTimesArticle.txt', mode='r')
allwords = textfile.read()
print(allwords)

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(allwords.lower())
print(tokens)

tokens = [token for token in tokens if token not in stopwords.words('english')]
print(tokens)

freq_dist = nltk.FreqDist(tokens)

print(freq_dist)
print(freq_dist.most_common(25))
freq_dist.plot(25)

