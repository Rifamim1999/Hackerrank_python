if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])        
    re = sorted(set([score for name,score in data]))[1]
    print('\n'.join(set([name for name, score in data if score == re])))
