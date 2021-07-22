import numpy as np






def sigma(q):
    
    pos = 0

    neg = 0
    res = 0.0
    for i in range(0, 100):
        res+= (-q)**i
        cond= (-q)**i
        if(cond>0):
            print("\t\t\t\tpos:",cond)
            pos+=cond
        else:
            print("neg:",cond)
            neg+=cond

    
    print("\t\t\t\tPos:",pos)
    print("neg:",neg)

    return res

def sigPrime(q):
    return 1/(1+q)

q = 0.5


print(sigma(q))
print(sigPrime(q))



#q = 0.1
"""
for j in range(1,100):
    print(sigma(q))
    print(sigPrime(q))
    q += j*(0.0005)
    print("\t\t",q)
"""

