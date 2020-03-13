from nltk.corpus import stopwords
import nltk

def one(t):
    raw=open(t).read()
    #r=raw.splitlines()
    #s=str(r).split(' ')
    words= raw.split()
    porter = nltk.PorterStemmer()
    stemmed_tokens = [porter.stem(t) for t in words]
    stop_words = set(stopwords.words('arabic'))
    voc = [w for w in stemmed_tokens if not w in stop_words]
    v=set(voc)
    #print(v)
    return v;

t='input.txt'
t1=one(t)