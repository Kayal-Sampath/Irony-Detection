fmax = open('max_arabic_data_for_ml.txt','w+')
fmin = open('min_arabic_data_for_ml.txt','w+')
fmin_max = open('min_max_arabic_data_for_ml.txt','w+')
classname=open('a.txt','r')
cname=classname.readlines()
for i in range(4024):
    content=open('min/min_word_for_line'+str(i)+'.txt','r')
    con=content.read()
    #print(con.strip('\n'))
    fmax.write(str(con.strip('\n')))
    c=str(cname[i]).split('\\t')
    #print(c[2])
    fmax.write(str(c[2]))
    
for i in range(4024):
    content=open('max/max_word_for_line'+str(i)+'.txt','r')
    con=content.read()
    #print(con.strip('\n'))
    fmin.write(str(con.strip('\n')))
    c=str(cname[i]).split('\\t')
    #print(c[2])
    fmin.write(str(c[2]))    
    
for i in range(4024):
    content=open('min_max/min_max_word_for_line'+str(i)+'.txt','r')
    con=content.read()
    #print(con.strip('\n'))
    fmin_max.write(str(con.strip('\n')))
    c=str(cname[i]).split('\\t')
    #print(c[2])
    fmin_max.write(str(c[2]))     