# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:10:36 2023

@author: Moule

n=9#int(input("请输入参与人数"))
m=3#int(input("请输入报到多少退出"))
x="x"
data=[]
for i in range(n):
    data.append([x+str(i),i+1])

for i in range(len(data)):
    if data[i][1]==n:
        data[i][1]=0

p=head=q=c=0
while n>1:
    c+=1    
    p=data[p][1]
    if c==m:
        q=p
        c=0
        p=data[p][1]
print(data)
print(data[p][0])"""
n=int(input("请输入参与人数"))
m=int(input("请输入报到多少退出"))
x="x"
data=[]
for i in range(n):
    data.append([x+str(i),i+1])

for i in range(len(data)):
    if data[i][1]==n:
        data[i][1]=0

q=p=head=0
c=0
while n>1:
    c+=1
    if c==x:
        data[q][1]=data[p][1]
        c=0
        n-=1
    q=p
    p=data[p][1]
print("最终剩下的人的编号",data[p][0])
    