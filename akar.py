#Algoritma menghitung akar
#programmer : Syahrial
#Tanggal : 05-Februari-2025

import math

# untuk menghitung akar dari suatu bilangan
def hitung_akar(bilangan):
    if bilangan < 0:
        return "Tidak bisa menghitung akar dari bilangan negatif"
    else:
        return math.sqrt(bilangan)

# Input dari pengguna
bilangan = float(input("Masukkan bilangan: "))

# Menampilkan hasil 
hasil = hitung_akar(bilangan)
print(f"Akar dari {bilangan} adalah {hasil}")
