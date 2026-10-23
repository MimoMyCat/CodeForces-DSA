n = int(input())
lst=[]
for i in range(n):
    word = input()
    if len(word)>10:
        lst.append(word[0]+str(len(word[1:-1]))+word[-1])
    else:
        lst.append(word)
for i in lst:
    print(i)


