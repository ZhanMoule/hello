# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:59:01 2023
队列的基操
@author: Moule

head=0;tail=0
a="ABCD";b=""
q=[""]*(len(a)+1)
for i in range(len(q)-1):   
    q[tail]=a[i]
    tail+=1
while head!=tail:
    print(q[head])
    head+=1
print(q)"""

s=input("请输入加密的字符串")
que=[""]*100
head=tail=0
for i in range(len(s)):
    que[tail]=s[i]
    tail+=1
while head!=tail:
    print(que[head],end='')
    head+=1
    if head<tail:
        que[tail]=que[head]
        head+=1;tail+=1
print("加密后的字符串为"+str(que))

    
    
