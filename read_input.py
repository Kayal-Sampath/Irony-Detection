fin=open('a.txt','r')
fout1=open('input.txt','w+')
f1=fin.readlines()
for i in range(len(f1)):
    ids=str(f1[i]).split('\\t')[0]
    #print(ids)
    content=str(f1[i]).split('\\t')[1]
    print(content)
    cname=str(f1[i]).split('\\t')[2]
    #print(cname.strip('\n'))
    fout1.write(ids)
    fout1.write('\t')
    fout1.write(cname.strip('\n'))
    fout1.write('\t')
    fout1.write('a')
    fout1.write('\t')
    fout1.write(content)
    fout1.write('\n')

