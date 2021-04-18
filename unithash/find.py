def get_unithash(n: int):
    int(n)
    if (n == 0):
        return 0
    elif (n % 9 == 0):
        return 9
    else:
        return n % 9

def set_unithash(num: str, l: int):
    sanitation=[]
    sanitation[:0]=num
    for i in range(0,len(sanitation)):
        if (sanitation[i].isdigit())==False:
            sanitation[i]=abs(ord(sanitation[i])-96)
    num = ''.join([str(j) for j in sanitation])
    hash = [(num[i:i+int(l)]) for i in range(0, len(num), int(l))]
    final_hash = []
    for i in range(0,len(hash)):
        final_hash.append(get_unithash(int(hash[i])))
    fin_hash = ''.join([str(i) for i in final_hash])
    return int(fin_hash)

#l = length of each group after number is broken
#num = the actual number to be hashed