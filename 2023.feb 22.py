# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#随机生成9个数并降序排序再生成随即一个整数插入到列表中

import random
a=[random.randint(0,100) for i in range(9)]+[0]
for j in range(len(a)):
    for p in range(j,len(a)):
        if a[j]<a[p]:
            a[j],a[p]=a[p],a[j]
b=random.randint(0,100)
for q in range(len(a)):
    if b>a[q]:
        b,a[q]=a[q],b
print(a)       
            
        

        
        
