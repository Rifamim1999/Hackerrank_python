if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    li = []
    for i in range(0,x+1):
    #li.append([i])
        for j in range(0,y+1):
        #li[i].append(j)
            for k in range(0,z+1):
            #li.append(k)
                if i+j+k != n:
                    result = [i,j,k]
                    li.append(result)
    print(li)
