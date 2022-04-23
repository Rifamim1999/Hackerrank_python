if __name__ == '__main__':
    s = input()
    a =0
    b=0
    c=0
    d=0
    e =0
    for i in s:
        if (i.isalnum() == True):
            a +=1
        elif (i.isalnum() == False):
            a =a
        if (i.isalpha() == True):
            b += 1
        elif (i.isalpha() == False):
            b = b
        if(i.isdigit() == True):
            c += 1
        elif(i.isdigit() == False):
            c = c
        if (i.islower() == True):
            d += 1
        if (i.isupper() == True):
            e += 1
    if a>0:
        print('True')
    if a == 0:
        print('False')
    if b>0:
        print('True')
    if b==0:
        print('False')
    if c>0:
        print('True')
    if c==0:
        print('False')
    if d>0:
        print('True')
    if d==0:
        print('False')
    if e>0:
        print('True')
    if e==0:
        print('False')
                
