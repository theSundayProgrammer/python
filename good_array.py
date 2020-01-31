# coding: utf-8
from math import gcd
def find_k1k2g(a,b,g=1):
    found = a-b==g or b-a==g
    ka=1
    kb=1
    a0 = a
    b0 = b
    if found:
       if a<b : ka = -1
       else: kb = -1
    while not found:
        if a0<b0 : 
            k = b0//a
            ka = (k+1)
            a0 = ka *a
            kb = -kb
        else:
            k = a0//b
            kb = k+1
            b0= kb *b
            ka = -ka
        found = a0-b0==g or b0-a0==g
    return (ka,kb)
   
def print_good_array(arr):
    multiples = []
    g0=gcd(arr[0],arr[1])
    multiples.append(find_k1k2g(arr[0],arr[1],g0))
    i =2
    while i < len(arr) and not g0==1:
        g1 = gcd(g0,arr[i])
        if g1 == arr[i]: multiples.clear()
        else: multiples.append(find_k1k2g(g0,arr[i],g1))
        g0=g1
        i+=1
    
    if g0 ==1 :    
        multiplier= 1
        while (len(multiples) > 1) :
            (k1,k2) = multiples.pop()
            i -=1 
            print(k2*multiplier,"*", arr[i], "+ " )
            multiplier*=k1
        (k1,k2) = multiples.pop()
        print(k2*multiplier,"*", arr[i-1], "+ ", k1*multiplier , "*",arr[i-2] )
    else:
        print("Bad Array")
        
if __name__ == "__main__" :
    print_good_array( [77,91,7,143,175])
