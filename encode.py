def odd(x):
    if x%2==0:
        return 0
    else:
        return 1
def flip(x):
    # print('x is',x)
    if x:
        return 0
    else:
        return 1
message=input()
errorpos=list(map(int,input().strip().split()))
# message='aman'
message=list(map(int,message.strip().split()))
len_message=len(message)
message=message+[1]+[0]*(26-len_message)
import numpy as np
message=np.reshape(np.array(message),(3,3,3))
# print(message)
# print(np.reshape(message,(1,27)))

# red_bit[(-1,2,3)]=3
red_bit=np.zeros((3,3,3))
a=np.sum(message,axis=1)
# print(red_bit[:,0,:])
b=np.sum(message,axis=2)
# print(red_bit[:,1,:])
c=np.sum(message,axis=0)
# print(red_bit[:,2,:])
# print(red_bit[:,:,2])
red_bit=np.array([a,b,c])
# print(red_bit)
for i in range(3):
    for j in range(3):
        for k in range(3):
            red_bit[i,j,k]=odd(red_bit[i,j,k])
to_send=np.reshape(message,(1,27)).tolist()[0]+list(map(int,np.reshape(red_bit,(1,27)).tolist()[0]))
if errorpos[0]!=-1:
    to_send[errorpos[0]]=flip(to_send[errorpos[0]])
if errorpos[1]!=-1:
    to_send[errorpos[1]]=flip(to_send[errorpos[1]])
print(''.join(list(map(str,to_send))))

# print(mat1)
