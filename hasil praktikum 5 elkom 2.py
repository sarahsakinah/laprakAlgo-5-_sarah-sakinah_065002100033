# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 16:41:31 2021

@author: HP
"""

print("@@@@ @@@ @@@@ @@@  @ @")
print("@    @ @ @  @ @ @  @ @")
print("@    @@@ @@@@ @@@  @ @")
print("@@@@ @@@ @@   @ @  @@@")
print("   @ @ @ @ @  @ @  @ @")
print("   @ @ @ @  @ @ @  @ @")
print("@@@@ @ @ @   @@ @  @ @")
print('=====HITUNGAN ANGKA=====')
jam1=float(input('waktu masuk kerja: '))
gaji = 175000
if jam1 >=9.00:
    print('selamat pagi')
if jam1 >=14.00:
    print('selamat siang')
    
jam2=float(input('waktu selesai kerja: '))
if jam2 >=17.00:
    print('selamat sore')
elif jam2 >=18.00:
    print('selamat sore')
elif jam2 - jam1 >=08.00:
    gaji=gaji
elif jam2 - jam1 >=08.59:
    sarah = int((jam2 - jam1)-8)
    gaji2 =((sarah)*15000)
    
sarah = int((jam2 - jam1)-8)
gaji2 =((sarah)*15000)

print('=====RINCIAN GAJI HARIAN=====')
print(f'waktu kerja      :{int(jam2 - jam1)} jam ( 09.00 sd 18.00)')
print(f'gaji per harian  :Rp.{gaji}')
print(f'lembur           :Rp.{gaji} ({sarah} jam x Rp.15000 )')
print(f'total gaji       :Rp.{(gaji)+gaji2}')
if jam2 - jam1<9.00:
    print('==========TERIMA KASIH==========')