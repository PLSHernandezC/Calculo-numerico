#!/usr/bin/env python3

def Error_absoluto(a,b):
    Error_absoluto=abs(a-b)

    return Error_absoluto
    
def Error_relativo(a,b):
    Error_relativo=abs((a-b)/a)

    return Error_relativo

if __name__ == "__main__":

#PRUEBA 

    x=5
    y=4

    print(Error_absoluto(x, y))
    print((Error_relativo(x, y)))

#PRUEBA2
    
    x=20_000
    y=19_999

    print(Error_absoluto(x, y))
    print(Error_relativo(x, y))