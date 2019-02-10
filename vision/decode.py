import numpy as np
from copy import deepcopy
def odd(x):
    if x%2==0:
        return 0
    else:
        return 1
def flip(x):
    if x:
        return 0
    else:
        return 1
def decode(full_message):
    full_message=list(map(int,list(full_message.strip())))
    message=full_message[0:27]
    received_message=deepcopy(message)
    red_bits=full_message[27:54]
    message=np.reshape(np.array(message),(3,3,3))
    # print(message)
    red_bits=np.reshape(np.array(red_bits),(3,3,3))
    # print(red_bits)
    apparent_red_bit=np.zeros((3,3,3))
    a=np.sum(message,axis=1)
    b=np.sum(message,axis=2)
    c=np.sum(message,axis=0)
    apparent_red_bit=np.array([a,b,c])
    for i in range(3):
        for j in range(3):
            for k in range(3):
                apparent_red_bit[i,j,k]=odd(apparent_red_bit[i,j,k])
    # print(apparent_red_bit)
    boole=0
    eq=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(red_bits[i,j,k]!=apparent_red_bit[i,j,k]):
                    eq=1
                orig_bit1=red_bits[0,i,k]
                orig_bit2=red_bits[1,i,j]
                orig_bit3=red_bits[2,j,k]
                present_bit1=apparent_red_bit[0,i,k]
                present_bit2=apparent_red_bit[1,i,j]
                present_bit3=apparent_red_bit[2,j,k]
                ans=0
                if(orig_bit1!=present_bit1):
                    ans+=1
                if(orig_bit2!=present_bit2):
                    ans+=1
                if(orig_bit3!=present_bit3):
                    ans+=1
                if(ans>=3):
                    boole=1
                    # print('i,j,k are',i,j,k)
                    message[i,j,k]=flip(message[i,j,k])
    if(boole==0):
        if eq==1:
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        orig_bit1=red_bits[0,i,k]
                        orig_bit2=red_bits[1,i,j]
                        orig_bit3=red_bits[2,j,k]
                        present_bit1=apparent_red_bit[0,i,k]
                        present_bit2=apparent_red_bit[1,i,j]
                        present_bit3=apparent_red_bit[2,j,k]
                        ans=0
                        if(orig_bit1!=present_bit1):
                            ans+=1
                        if(orig_bit2!=present_bit2):
                            ans+=1
                        if(orig_bit3!=present_bit3):
                            ans+=1
                        if(ans>=2):
                            # boole=1
                            # print('i,j,k are',i,j,k)
                            message[i,j,k]=flip(message[i,j,k])
    message=message.reshape((1,27)).tolist()[0]
    message.reverse()
    ans=list()
    for i,val in enumerate(message):
        if val==1:
            ans=message[i+1:]
            ans.reverse()
            break
    print(received_message)
    print(message)
    return ''.join(list(map(str,ans)))

