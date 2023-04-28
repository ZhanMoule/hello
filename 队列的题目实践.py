# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 14:37:22 2023
依然队列    PS：求队列中的所在元素长度时可采用公式 :(tail+head-n)%n
题目：出一张，一张放后面，出2张，一张放后面，出三张，一张放后面
@author:Moule

s="234567890JQKA"
head=tail=0
n=len(s)
b=0;c=1
q=[""]*100
for i in range(len(s)):
    q[tail]=s[i]
    tail+=1
while head!=tail:
    if b==c:
        print(q[head],end='')
        b=1
        c+=1
        head+=1
    else:
        q[tail]=q[head]
        tail+=1
        head+=1
        b+=1
print(q)

q=list("234567890JQKA")
head=tail=0
c=1;res=''
while head!=tail:
    i=1
    while i<=c and head!=tail:
        res+=q[head]
        head+=1
        i+=1
    if head!=tail:
        q[tail]=q[head]
        tail+=1
        head+=1
    c+=1
print(res)"""
#题目二-------------------------------------------------
#银行叫号系统：单窗口队列
head=tail=0
q=[""]*100
a=["A1","A3","A4","A5","A6","A7","A8","A9"]
caozuo={1:"取号",2:""}
while head!=tail:
    b=input("请输入操作编号1")
               
        
    
    
    

