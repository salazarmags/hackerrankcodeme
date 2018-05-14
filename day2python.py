if __name__ == '__main__':
    N = int(input())
    commands = [c = input() for i in N]
    
    ls = []
    
    l = commands[i].split()
    for i in range(N):
        c = input().split()
        if c[0] == "insert":
            l[c[1]] = c[2]
            
        elif c[0] == "remove":
            l.remove(c[1])
        elif c[0] ==
    
