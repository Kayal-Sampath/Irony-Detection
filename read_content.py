fin=open('a.txt','r')
fout1=open('input.txt','w+')
fout2=open('output.txt','w+')
f1=fin.readlines()
for i in range(4024):
    content=str(f1[i]).split('\\t')[1]
    print(content)
    cname=str(f1[i]).split('\\t')[2]
    print(cname)
    fout1.write(content)
    fout1.write('\n')
    fout2.write(cname)

        
        