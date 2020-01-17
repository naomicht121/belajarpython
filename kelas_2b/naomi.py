import csv
import os
import matplotlib.pyplot as plt
import requests
import sqlite3

class daftar(object):
    def siswa(self):
        with open('bio.csv', 'r') as filecsv:
            datafile = csv.reader(filecsv)
            for data in datafile:
                print(data)
    
    def __init__(Nama,Kelas,Sekolah,Kota):
        self.Nama = Nama
        self.Kelas = Kelas
        self.Sekolah = Sekolah
        self.Kota = Kota

    def EXO():
        print "WE ARE ONE"

    def getDBConfig():
        config = {
            "driver":"sqlite3",
            "name":"testing.db",
            "path":"/home/user/Documents"
        }

        return config
    
    def tampilkan_profil(self):
        print("Nama :", self.Nama)
        print("Kelas :", self.Kelas)
 
    def getName(id):
        if id == 1:
            name = "Chanyeol"
        elif id == 2:
            name = "Baekhyun"
        elif id == 3:
            name = "Kai"

        return name

    def dataq(self): # methode
        print('EXO')

        tampil = Daftar() # instansiasi

        tampil.dataq() # memanggil nama method

    
    def keterangan(self):
        nama = "Chanyeol"
        umur = "27"
        tgl_lahir = "27-11-1992"
        
        print(nama, umur, tgl_lahir)

    def tambah_baris(self):
        with open('bio.csv', mode='a') as csv_file:
    # menentukan label
            fieldnames = ['Nama', 'Kelas', 'Sekolah', 'Kota']
    
    # membuat objek writer
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # menulis baris ke file CSV
        writer.writeheader()
        writer.writerow({'Nama': 'Baekhyun', 'Kelas': '12 IPS', 'Sekolah': 'SMA N 1 Busan', 'Kota': 'Busan'})
        writer.writerow({'Nama': 'Chanyeol', 'Kelas': '12 IPA', 'Sekolah': 'MAN 2 Seoul', 'Kota': 'Seoul})    
    print("Writing Done!")