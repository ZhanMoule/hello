# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:44:11 2023

@author: jsj2
"""
#做一个自定义函数是两个列表a和b实现相加合并输出

def sb(a,b):
    c=[]
    c=a+b
    for i in range(len(c)):
        for j in range(i,len(c)):
            if c[i]<c[j]:
                c[i],c[j]=c[j],c[i]
    return c
a=list(input("请输入一个原始列表1"))
b=list(input("请输入一个原始列表2"))
print(sb(a,b))
                
    