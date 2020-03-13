fileinput=open('test_results.txt','r')
fi=fileinput.readlines()

for i in range(len(fi)):
    f=fi[i].split('\t')
    if (f[0] >= f[1]) :
        print('0') 
    else:
        print('1')