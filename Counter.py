# -*- coding: utf-8 -*-
"""
Counting device
Created on Fri May 13 13:41:51 2022
@author: Lishu Zhang
"""
raw = open('Yanchao1.txt').read().split() 
# 'your file.txt' --> make sure it's in the right directory folder
#  it is imported as a list of strings

## start from here: you only need to change the content in s.count(''). Each s.count('') counts for one combination. The basic codes are:
# sum = 0
# for s in raw:
#     sum = sum +s.count('')+s.count('')+s.count('') 
#     print(sum)
## You can also bring print(sum) outside the loop.

# For instance, to count the total occurance of the following combinations: AGG, TGG, CGG, GGG, CCA, CCT, CCG, CCC
sum=0
for s in raw:
    sum = sum +s.count('AGG')+s.count('TGG')+s.count('CGG')+s.count('GGG')+s.count('CCA')+s.count('CCT')+s.count('CCG')+s.count('CCC')
    print(sum)

# for TTTA, TTTC, TTTG, TAAA, CAAA, GAAA
sum2=0
for s in raw:
    sum2 = sum2 +s.count('TTTA')+s.count('TTTC')+s.count('TTTG')+s.count('TAAA')+s.count('CAAA')+s.count('GAAA')
    print(sum2)
    
# Or for TTA, TTC, TTG, TAA, CAA, GAA
sum3=0
for s in raw:
    sum3 = sum3 +s.count('TTA')+s.count('TTC')+s.count('TTG')+s.count('TAA')+s.count('CAA')+s.count('GAA')
    print(sum3)