# daftar deklarasi fungsi
def baca_data(filename):
    # fungsi digunakan untuk membaca file teks, kemudian merubah ke dalam
    # tipe data terstruktur
    file = open (filename, "r")

    dict_minggu1 = {} # key adalah nim, dan value adalah jumlah kehadiran mahasiswa
    dict_minggu2 = {}
    dict_minggu3 = {}
    dict_minggu4 = {}
    dict_minggu5 = {}
    dict_minggu6 = {}
    dict_minggu7 = {}

    teks = file.readline().replace("\n","")
    while teks != "" :
        list_kata = teks.split() # indeks 0: Nim, 1:minggu ke-1, 2:....

        if list_kata[1] in dict_minggu1:
            dict_minggu1[list_kata[1]].append(list_kata[0])
        else:
            dict_minggu1[list_kata[1]] = [ list_kata[0] ]

        if list_kata[2] in dict_minggu2:
            dict_minggu2[list_kata[2]].append(list_kata[0])
        else:
            dict_minggu2[list_kata[2]] = [ list_kata[0] ]

        if list_kata[3] in dict_minggu3:
            dict_minggu3[list_kata[3]].append(list_kata[0])
        else:
            dict_minggu3[list_kata[3]] = [ list_kata[0] ]

        if list_kata[4] in dict_minggu4:
            dict_minggu4[list_kata[4]].append(list_kata[0])
        else:
            dict_minggu4[list_kata[4]] = [ list_kata[0] ]

        if list_kata[5] in dict_minggu5:
            dict_minggu5[list_kata[5]].append(list_kata[0])
        else:
            dict_minggu5[list_kata[5]] = [ list_kata[0] ]

        if list_kata[6] in dict_minggu6:
            dict_minggu6[list_kata[6]].append(list_kata[0])
        else:
            dict_minggu6[list_kata[6]] = [ list_kata[0] ]

        if list_kata[7] in dict_minggu7:
            dict_minggu7[list_kata[7]].append(list_kata[0])
        else:
            dict_minggu7[list_kata[7]] = [ list_kata[0] ]
            
        teks = file.readline().replace("\n","")

    file.close()
    data_kehadiran = [dict_minggu1, dict_minggu2, dict_minggu3, dict_minggu4, dict_minggu5, dict_minggu6, dict_minggu7]
    return data_kehadiran

def print_data(data):
    # fungsi untuk menampilkan data data_kehadiran
    list_minggu = ["Minggu-1", "Minggu-2", "Minggu-3", "Minggu-4", "Minggu-5", "Minggu-6", "Minggu-7"]
    i = 0
    for elemen in data:
        print("Kehadiran:",list_minggu[i])
        for key in elemen:
            print("NIM -",key,"=",elemen[key])
        print("\n")
        i += 1

# Jawaban untuk point b (belum selesai)
def report(data, indeks, urutan_minggu):
    list_minggu = ["Minggu-1", "Minggu-2", "Minggu-3", "Minggu-4", "Minggu-5", "Minggu-6", "Minggu-7"]
    idx = list_minggu.index(urutan_minggu)
     
    if indeks == 1 <=5 in data[idx]:
        # tampilkan jumlah mahasiswa yang diperbolehkan ujian
        print("NIM yang diperbolehkan mengikuti ujian", data[idx][indeks])
    else:
        # tampilkan jumlah mahasiswa yang tidak diperbolehkan ujian
        print("NIM yang tidak diperbolehkan mengikuti ujian", data[idx][indeks])
        
    
# main program
nama_file = "contoh_file.txt"
data_kehadiran = baca_data(nama_file)
print_data(data_kehadiran)

print("Report Mahasiswa:")
urutan_minggu, indeks = input().split()
report(data_kehadiran, indeks, urutan_minggu)

