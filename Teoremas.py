#!/usr/bin/env python3

def existe_valor_inter (f,a,b):
    return f(a)*f(b)<0
    
if __name__ == '__main__':
    f= lambda x :x**2-4

#PRUEBA
    a=0
    b=5
    print(valor_inter(f, a, b))