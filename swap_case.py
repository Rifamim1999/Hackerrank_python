def swap_case(s):
    b = ''
    for i in s:
        if i.isupper() == True:
            b= b+i.lower()
        elif i.islower() == True:
            b=b+i.upper()
        else:
            b=b+i
    
    return b

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
