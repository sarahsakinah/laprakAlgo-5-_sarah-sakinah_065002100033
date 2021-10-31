# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 17:51:02 2021

@author: HP
"""

print("@@@@ @@@ @@@@ @@@  @ @")
print("@    @ @ @  @ @ @  @ @")
print("@    @@@ @@@@ @@@  @ @")
print("@@@@ @@@ @@   @ @  @@@")
print("   @ @ @ @ @  @ @  @ @")
print("   @ @ @ @  @ @ @  @ @")
print("@@@@ @ @ @   @@ @  @ @")
print("====DERET FIBONACCI====")

sarah = int(input("masukkan jumLah bilangan: "))

bil1=int(input("masukkan bilangan kesatu: "))
bil2=int(input("masukkan bilangan kedua: "))
for i in range(sarah):
  v=bil1
    
  x = bil1+bil2
  bil1=bil2
  bil2=x
  print(v) 