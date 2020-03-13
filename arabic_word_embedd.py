import nltk
from nltk.corpus import stopwords
import gensim
import re
model = gensim.models.Word2Vec.load('ar_wiki_word2vec')

def write_vector(w,i):
    print(w)
    fout=open('word_embeddings_2/word_for_line'+str(i)+'.txt','a+')
    fout.write(str(w))


def clean_str(text):
    #print('clean')
    search = ["أ","إ","آ","ة","_","-","/",".","،"," و "," يا ",'"',"ـ","'","ى","\\",'\n', '\t','&quot;','?','؟','!']
    replace = ["ا","ا","ا","ه"," "," ","","",""," و"," يا","","","","ي","",' ', ' ',' ',' ? ',' ؟ ',' ! ']
    
    #remove tashkeel
    p_tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    text = re.sub(p_tashkeel,"", text)
    
    #remove longation
    p_longation = re.compile(r'(.)\1+')
    subst = r"\1\1"
    text = re.sub(p_longation, subst, text)
    
    text = text.replace('وو', 'و')
    text = text.replace('يي', 'ي')
    text = text.replace('اا', 'ا')
    for i in range(0, len(search)):
        text = text.replace(search[i], replace[i])
    
    #trim    
    text = text.strip()
    return text

def word_embedd(v,i):
    t=[]
    #print('word_embedd')
    for x in v:
        word = clean_str(x)
        try:
            word_vector = model.wv[word]
            t.append(word_vector)            
            #print(type(word_vector))
            #write_vector(word_vector,i)
            #print(word_vector)
        except KeyError:
            #print("not in voc")
            continue;
    fout2=open('min_max/min_max_word_for_line'+str(i)+'.txt','a+')        
    for k in range(0,300):
        #print('min max')
        l=len(t)
        q=0
        q1=1.7976931348623157e+308
        for m in range(0,l-1):
            q=max(t[int(m)][int(k)],t[int(m+1)][int(k)],q)
            q1=min(t[int(m)][int(k)],t[int(m+1)][int(k)],q1)
        fout2.write(str(q))
        fout2.write(' ')
        fout2.write(str(q1))
        fout2.write(' ')
    fout2.write('\n')

    fout3=open('min/min_word_for_line'+str(i)+'.txt','a+')        
    for k in range(0,300):
        #print('max')
        l=len(t)
        q=0
        for m in range(0,l-1):
            q=max(t[int(m)][int(k)],t[int(m+1)][int(k)],q)
        fout3.write(str(q))
        fout3.write(' ')
    fout3.write('\n')

    fout4=open('max/max_word_for_line'+str(i)+'.txt','a+')        

    for k in range(0,300):
        #print('max')
        l=len(t)
        q1=1.7976931348623157e+308
        for m in range(0,l-1):
            q1=min(t[int(m)][int(k)],t[int(m+1)][int(k)],q1)
        fout4.write(str(q1))
        fout4.write(' ')
    fout4.write('\n')

def one(t):
    #print('one')
    raw=open(t).read()
    r=raw.splitlines()
    for i in range(4024):
        s=str(r[i]).split(' ')
        #print(r[i])
        #print(s)
        #words= raw.split()
        #print(len(s))
        #print(s)
        porter = nltk.PorterStemmer()
        stemmed_tokens = [porter.stem(t) for t in s]
        stop_words = set(stopwords.words('arabic'))
        voc = [w for w in stemmed_tokens if not w in stop_words]
        #print(voc)
        word_embedd(voc,i)
        print(i)

t='input1.txt'
t1=one(t)


