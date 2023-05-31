class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
    
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)
    
    def hapus_mahasiswa(self, mahasiswa):
        if mahasiswa in self.DaftarMahasiswa:
            self.DaftarMahasiswa.remove(mahasiswa)
            print("Mahasiswa", mahasiswa.nama, "telah dihapus dari jurusan", self.NamaJurusan)
        else:
            print("Mahasiswa", mahasiswa.nama, "tidak terdaftar dalam jurusan", self.NamaJurusan)
    
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        if len(self.DaftarMahasiswa) == 0:
            print("Tidak ada mahasiswa yang terdaftar.")
        else:
            for mahasiswa in self.DaftarMahasiswa:
                mahasiswa.tampilkan_info()


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []
    
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)
    
    def hapus_jurusan(self, jurusan):
        if jurusan in self.DaftarJurusan:
            self.DaftarJurusan.remove(jurusan)
            print("Jurusan", jurusan.NamaJurusan, "telah dihapus dari universitas", self.NamaUniversitas)
        else:
            print("Jurusan", jurusan.NamaJurusan, "tidak terdaftar dalam universitas", self.NamaUniversitas)
    
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        if len(self.DaftarJurusan) == 0:
            print("Tidak ada jurusan yang tersedia.")
        else:
            for jurusan in self.DaftarJurusan:
                print(jurusan.NamaJurusan)


# 2. Buat objek Universitas dengan nama "XYZ University"
universitas = Universitas("XYZ University")

# 3. Buat objek Jurusan dengan nama "Teknik Informatika" dan tambahkan ke dalam Universitas XYZ
jurusan = Jurusan("Teknik Informatika")
universitas.tambah_jurusan(jurusan)

# 4. Buat objek Mahasiswa dengan nama "M Hisbulah Endima T", NIM "G1A022034", dan masukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa = Mahasiswa("M Hisbulah Endima T", "G1A022034", jurusan)
jurusan.tambah_mahasiswa(mahasiswa)

# 5. Tampilkan daftar jurusan di Universitas XYZ
universitas.tampilkan_daftar_jurusan()

# 6. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan.tampilkan_daftar_mahasiswa()

# 7. Hapus mahasiswa dari Jurusan Teknik Informatika
jurusan.hapus_mahasiswa(mahasiswa)

# 8. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ setelah mahasiswa dihapus
jurusan.tampilkan_daftar_mahasiswa()

# 9. Hapus jurusan dari Universitas XYZ
universitas.hapus_jurusan(jurusan)

# 10. Tampilkan daftar jurusan di Universitas XYZ setelah jurusan dihapus
universitas.tampilkan_daftar_jurusan()