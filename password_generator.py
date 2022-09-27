#!/usr/bin/env python3

import random
from string import digits, ascii_letters, punctuation

def symbollist():
    symbols = [ascii_letters, 
            digits, punctuation,]

    symbollist = []

    unsupportedIBM = '|<\"\'>\\ '

    for string in symbols:
        for item in string:
            if item not in unsupportedIBM:
                symbollist.append(item)

    return(symbollist)



def rand_pass_gen():
    
    symbols = symbollist()
    
    while True:
        
        n = input('''Input an integer password length, or type "exit" to exit the program: ''')
        if n == 'exit':
            break
        else: 
            try:
                n = int(n)
                print(f'Your random {n}-digit password is: ', ''.join(random.sample(symbols, n)))
            except:
                print('Please make sure the value is an integer and try again.')

            
rand_pass_gen()