
f2=open('allvector.txt','w+')

for i in range(4024):
    f1=open('word_embeddings/word_for_line'+str(i)+'.txt','r')
    allwe=f1.read()
    allwe1=allwe.replace('[','')
    allwe2=allwe1.replace('][','')
    allwe3=allwe2.replace(']','')
    a4=allwe3.replace('\n','')
    a6=a4.replace(' ',',')
    a7=a6.replace(',,',',')
    a8=a7.replace(',,',',')
    f2.write(str(a8))
    f2.write('\n')