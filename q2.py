def bfs(n, graph):
    outp = []
    in_d = [0]*n 
  
    for i in range(n):
        for j in graph[i]: 
            in_d[j]+=1

    fila = []
    for i in range(len(in_d)): 
        if in_d[i] == 0: 
            fila.append(i)
            outp.append(i)
    
    cnt = 0

    while(fila):
        k = fila.pop(0) 

        for v in graph[k]: 
            in_d[v] -= 1

            if in_d[v] == 0: 
                fila.append(v)
                outp.append(v)
        cnt+=1

    if cnt == n: 
        return outp
    else: 
        return False

def main():
    graph = [[]]*8

    graph[0] = [3]
    graph[1] = [2]
    graph[2] = [6]
    graph[3] = [5]
    graph[4] = [6]
    graph[5] = [6, 7]
    graph[6] = [7]
    graph[7] = []

    resp = bfs(8, graph)
    if resp:
        print(resp)
    else:
        print('Impossível carregar dependências, ciclo detectado')

    
main()