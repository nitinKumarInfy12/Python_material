# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:53:59 2019

@author: JSin24
"""

def add(a,b):
   return int(a) + int(b)
    
def sub(a,b):
   return int(a) - int(b)
    
def default(a,b):
    return 'Not supported'
    
opcodes ={'+': add, '-':sub, '%'}
exp=input('enter an expression:')

num1,op,num2=exp.split()
func=opcodes.get(op, default)
result=func(num1,num2)

print ('{} {} {}={}'.format(num1,op,num2,result))