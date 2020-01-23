
def overlapStart(s1, s2):
    i = 1
    cnt = 0
    tam2 = len(s2)

    while i < len(s1) and tam2-i > 0:
        #print('For {} and {}: {} and {}'.format(s1, s2, s1[0:i], s2[tam2-i:]))
        if s1[0:i] == s2[tam2-i:]:
            cnt=i
        i+=1
    return cnt

def main():
    strings = []

    while True:
        try:
            a = input()
            strings.append(a)
        except EOFError:
            break
    #print(strings)
    #lengthOver = []
    while len(strings) != 1:
        lengthOver = 0
        bLenghOver = 0
        toMerge = []
        for i in strings:
            for j in set(strings)-set(i):
                lengthOver = overlapStart(i, j)
                if(lengthOver > bLenghOver):
                    bLenghOver = lengthOver
                    toMerge = [j, i]
                #lengthOver.append((i, j, overlapStart(i, j)))
        
        merged = toMerge[0] + toMerge[1][bLenghOver:]
        strings.remove(toMerge[0])
        strings.remove(toMerge[1])
        strings.append(merged)

    print(strings[0])
    
    
main()