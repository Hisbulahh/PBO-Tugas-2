# PBO-Tugas-2

Dalam implementasi ini, tiga kelas objek yang diminta telah diimplementasikan dengan benar. Objek Mahasiswa memiliki atribut nama, nim, dan jurusan. Objek Jurusan memiliki atribut nama jurusan dan daftar mahasiswa. Objek Universitas memiliki atribut nama universitas dan daftar jurusan.

Andi dapat menggunakan program ini untuk mengelola data mahasiswa dan jurusan di Universitas XYZ. Setelah menjalankan program, daftar jurusan yang ada di universitas akan ditampilkan, dan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika juga akan ditampilkan.

lalu dalam Dalam pengembangan ini, ditambahkan dua metode baru: hapus_mahasiswa() pada kelas Jurusan untuk menghapus mahasiswa dari daftar mahasiswa dan hapus_jurusan() pada kelas Universitas untuk menghapus jurusan dari daftar jurusan.

Setelah menjalankan program, akan ditampilkan daftar jurusan dan daftar mahasiswa dalam Jurusan Teknik Informatika di Universitas XYZ. Kemudian, salah satu mahasiswa akan dihapus dari jurusan, dan daftar mahasiswa akan ditampilkan kembali. Selanjutnya, jurusan Teknik Informatika akan dihapus dari universitas, dan daftar jurusan akan ditampilkan lagi setelah penghapusan.

Berikut adalah penjelasan untuk setiap bagian dari kode:

Kelas Mahasiswa:

Kelas ini memiliki atribut nama, nim, dan jurusan.
Metode __init__() digunakan untuk menginisialisasi atribut dengan nilai yang diberikan saat pembuatan objek.
Metode tampilkan_info() digunakan untuk menampilkan informasi mahasiswa, yaitu nama, NIM, dan nama jurusan.
Kelas Jurusan:

Kelas ini memiliki atribut NamaJurusan dan DaftarMahasiswa.
Metode __init__() digunakan untuk menginisialisasi atribut dengan nilai yang diberikan saat pembuatan objek. DaftarMahasiswa diinisialisasi sebagai list kosong.
Metode tambah_mahasiswa() digunakan untuk menambahkan objek Mahasiswa ke dalam DaftarMahasiswa.
Metode hapus_mahasiswa() digunakan untuk menghapus objek Mahasiswa dari DaftarMahasiswa jika objek tersebut ada di dalamnya.
Metode tampilkan_daftar_mahasiswa() digunakan untuk menampilkan daftar mahasiswa yang terdaftar dalam jurusan.
Kelas Universitas:

Kelas ini memiliki atribut NamaUniversitas dan DaftarJurusan.
Metode __init__() digunakan untuk menginisialisasi atribut dengan nilai yang diberikan saat pembuatan objek. DaftarJurusan diinisialisasi sebagai list kosong.
Metode tambah_jurusan() digunakan untuk menambahkan objek Jurusan ke dalam DaftarJurusan.
Metode hapus_jurusan() digunakan untuk menghapus objek Jurusan dari DaftarJurusan jika objek tersebut ada di dalamnya.
Metode tampilkan_daftar_jurusan() digunakan untuk menampilkan daftar jurusan yang ada di universitas.
Pembuatan Objek:

Membuat objek Universitas dengan nama "XYZ University".
Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ.
Membuat objek Mahasiswa dengan nama "M Hisbulah Endima T", NIM "G1A022034", dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ.
Menampilkan Daftar Jurusan di Universitas XYZ:

Memanggil metode tampilkan_daftar_jurusan() pada objek universitas untuk menampilkan daftar jurusan yang ada di Universitas XYZ.
Menampilkan Daftar Mahasiswa dalam Jurusan Teknik Informatika di Universitas XYZ:

Memanggil metode tampilkan_daftar_mahasiswa() pada objek jurusan untuk menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ.
Menghapus Mahasiswa dari Jurusan Teknik Informatika:

Memanggil metode hapus_mahasiswa() pada objek jurusan untuk menghapus objek Mahasiswa dari Jurusan Teknik Informatika.
Menampilkan Daftar Mahasiswa dalam Jurusan Teknik Informatika di Universitas XYZ setelah Mahasiswa dihapus:

Memanggil metode tampilkan_daftar_mahasiswa() pada objek jurusan untuk menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika
