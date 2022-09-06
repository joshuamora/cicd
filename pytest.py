# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:35:07 2022

@author: jmoraaco
"""

import add_function 
import multiply_function

def main():
    
    a=3
    b=4
    c=add_function.add(a, b)
    print("ADD function test:  A= ",a," B= ",b,"C= ",c)
    
    c=multiply_function.multiply(a, b)
    
    print("MULTIPLY function test: A= ",a," B= ",b,"C= ",c)

if __name__ == "__main__":
    main()