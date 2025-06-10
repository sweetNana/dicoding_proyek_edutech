# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000 dan dikenal sebagai salah satu kampus unggulan dalam mencetak lulusan berkualitas di berbagai bidang keilmuan. Dengan reputasi yang telah dibangun selama lebih dari dua dekade, institusi ini menjadi magnet bagi calon mahasiswa yang ingin menapaki jenjang pendidikan tinggi dengan harapan masa depan yang lebih cerah.

Namun, di balik citra positif dan pencapaian tersebut, tersimpan tantangan serius yang tengah dihadapi—tingginya tingkat mahasiswa yang tidak menyelesaikan studi (dropout). Masalah ini tidak sekadar menjadi persoalan administratif atau angka statistik semata, melainkan mengindikasikan adanya potensi ketidakefektifan dalam berbagai aspek proses pendidikan, mulai dari penerimaan mahasiswa, proses belajar mengajar, hingga sistem pendampingan akademik.

Fenomena ini berdampak langsung terhadap tingkat kelulusan serta citra institusi di mata publik, terutama calon mahasiswa dan mitra strategis. Untuk itu, diperlukan pendekatan berbasis data yang komprehensif guna memahami akar masalah dan mengembangkan strategi pencegahan yang efektif. Dengan pemanfaatan data historis mahasiswa, Jaya Jaya Institut memiliki peluang untuk membangun sistem prediktif yang dapat membantu mengidentifikasi risiko dropout lebih awal dan memberikan intervensi yang tepat waktu.

## Permasalahan Bisnis

1. Tingginya angka mahasiswa yang tidak menyelesaikan studi tepat waktu (dropout), yaitu mencapai 32,1% dari total mahasiswa terdaftar, menjadi tantangan utama yang berdampak pada reputasi institusi.
2. Belum tersedianya sistem prediktif yang mampu mendeteksi secara dini mahasiswa dengan risiko tinggi untuk dropout, sehingga intervensi akademik sulit dilakukan secara tepat waktu.
3. Masih sulitnya mengidentifikasi faktor-faktor kunci yang paling memengaruhi keputusan mahasiswa untuk berhenti studi, terutama dalam konteks sosial-ekonomi, latar belakang pendidikan, dan performa akademik awal.
4. Monitoring kinerja akademik mahasiswa secara menyeluruh dan efisien masih menjadi tantangan, terutama dalam menggabungkan data dari berbagai sumber untuk mendukung pengambilan keputusan berbasis data.

## Cakupan Proyek

Proyek ini akan mencakup rangkaian proses analisis data dan pengembangan solusi prediktif untuk mengatasi masalah dropout mahasiswa, dengan rincian sebagai berikut:
1. Eksplorasi dan Analisis Data Awal
    Melakukan eksplorasi data (exploratory data analysis/EDA) guna memahami pola dan karakteristik mahasiswa, termasuk distribusi demografis, performa akademik, serta atribut sosial-ekonomi.
2. Pra-pemrosesan dan Transformasi Data
    Membersihkan, memfilter, dan mentransformasi data agar siap digunakan dalam pemodelan machine learning, termasuk penanganan data yang hilang, encoding kategori, dan normalisasi fitur.
3. Pengembangan Model Prediktif
    Membangun dan mengevaluasi model klasifikasi untuk memprediksi potensi dropout mahasiswa serta mengevaluasi faktor-faktor yang berkontribusi terhadap keberhasilan atau kegagalan studi.
4. Visualisasi dan Dashboard Interaktif
    Mendesain dashboard interaktif sebagai media visualisasi hasil analisis dan prediksi, guna mendukung pengambilan keputusan oleh pihak manajemen akademik secara lebih informatif dan real-time.
5. Validasi Model dan Pengujian Prototipe
    Melakukan pengujian terhadap kinerja model dan menyusun prototipe sistem berbasis machine learning sebagai proof of concept dalam konteks deteksi dini risiko dropout mahasiswa.

## Persiapan

### Sumber data
Dataset yang digunakan dalam proyek ini adalah [Dataset Internal Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv), yang berisi informasi akademik, demografis, dan sosial-ekonomi mahasiswa. Dataset ini telah dianonimkan untuk menjaga privasi dan keamanan data.

### Setup environment
1. Aktifkan Conda Environment
Pastikan environment Conda sudah terbuat, lalu aktifkan dengan perintah:
```conda create -n submission-edutech python=3.11```
```conda activate submission-edutech```

2. Install Dependencies
Pasang semua dependensi Python yang diperlukan:
```pip install -r requirements.txt```

### Menjalankan Analisis Data (notebook_edutech.ipynb)
1. Pastikan semua dependensi, packages, dan library yang dibutuhkan telah terinstal. Daftar lengkap dependensi dapat dilihat pada file requirements.txt.
2. Jalankan file notebook_edutech.ipynb untuk melakukan analisis data, menampilkan visualisasi, serta memperoleh temuan dan insight terkait attrition.

### Menajalankan Prediksi
Run file prediction.py pada environment yang sudah dijalankan sebelumnya. 
```python main.py```

### Setup Metabase (Visualisasi Dashboard)
Metabase akan digunakan untuk membuat visualisasi interaktif dari hasil analisis.       
1. Pastikan Docker telah terinstal di perangkat Anda
2. Tarik image Metabase versi 0.46.4 dengan perintah berikut di terminal Docker
```docker pull metabase/metabase:v0.46.4```
3. Jalankan container Metabase dengan perintah:
```docker run -p 3000:3000 --name metabase metabase/metabase```
4. Setelah container berjalan, akses Metabase melalui browser di alamat http://localhost:3000. 
5. Login menggunakan kredensial berikut:
    - Username: root@mail.com
    - Password: root123

## Business Dashboard
Dashboard ini dirancang untuk membantu pihak manajemen akademik dalam memantau dan mengevaluasi status mahasiswa (Dropout, Enrolled, Graduate) berdasarkan data historis. Di dalamnya terdapat visualisasi interaktif seperti:
1. Distribusi Status Mahasiswa
    Menampilkan perbandingan jumlah mahasiswa berdasarkan status akhir mereka.
2. Tren Performa Akademik dan Keadaan Ekonomi
    - Nilai penerimaan dan nilai semester sangat berpengaruh terhadap kelulusan. Mahasiswa yang dropout memiliki nilai jauh lebih rendah dibanding yang lulus. 
    - Kondisi keuangan mahasiswa juga sangat menentukan: proporsi mahasiswa dropout yang tidak melunasi biaya dan tidak menerima beasiswa jauh lebih tinggi.
    - Mahasiswa yang memiliki hutang lebih rentan untuk dropout.
3. Top 10 Fitur Paling Berpengaruh
    Menyajikan 10 variabel paling penting dalam menentukan status mahasiswa, seperti jumlah mata kuliah yang lulus, nilai semester awal, usia saat pendaftaran, dan status pembayaran kuliah. Grafik ini membantu pihak akademik mengidentifikasi faktor utama yang memengaruhi keberhasilan mahasiswa, sehingga dapat dilakukan intervensi dini.
4. Kondisi Ekonomi Makro
    Kondisi ekonomi makro seperti tingkat pengangguran dan inflasi sedikit berkontribusi, namun efeknya tidak sebesar faktor akademik dan ekonomi individu.

## Conclusion

Berdasarkan analisis, diketahui bahwa 32,1% mahasiswa mengalami dropout, dan sebagian besar dari mereka memiliki nilai akademik semester pertama dan kedua yang rendah, serta proporsi pelunasan biaya yang lebih kecil (rata-rata hanya 68%). Di sisi lain, mahasiswa yang berhasil lulus umumnya menunjukkan nilai akademik yang lebih tinggi, tingkat pelunasan biaya hampir sempurna (99%), dan proporsi beasiswa yang lebih tinggi.

Model analisis fitur juga menunjukkan bahwa faktor akademik seperti jumlah mata kuliah yang disetujui dan nilai pada semester pertama dan kedua menjadi indikator paling berpengaruh terhadap keberhasilan studi. Faktor ekonomi seperti status pembayaran biaya kuliah dan penerimaan beasiswa juga turut berkontribusi terhadap keputusan mahasiswa untuk melanjutkan atau berhenti studi.

## Rekomendasi Action Items

1. Bangun Sistem Peringatan Dini (Early Warning System)
    Terapkan dashboard prediktif yang memanfaatkan data akademik (nilai, evaluasi, jumlah mata kuliah lulus) dan data keuangan (status pelunasan biaya kuliah) untuk mengidentifikasi mahasiswa dengan risiko tinggi dropout.
2. Lakukan Intervensi Akademik Proaktif
    - Jadwalkan sesi bimbingan akademik secara rutin bagi mahasiswa yang terdeteksi memiliki performa rendah pada semester awal.
    - Tawarkan program remedial atau tutoring khusus untuk mata kuliah dengan tingkat kegagalan tinggi.
3. Tingkatkan Akses Beasiswa & Dukungan Finansial
    - Identifikasi mahasiswa dari latar belakang ekonomi rentan dan perluas cakupan beasiswa berbasis kebutuhan (need-based).\
    - Evaluasi ulang kebijakan pembayaran biaya agar lebih fleksibel (misalnya sistem cicilan atau grace period).
4. Pantau Performa Secara Terintegrasi
    - Satukan data dari berbagai sistem (akademik, keuangan, kehadiran, evaluasi dosen) ke dalam satu dashboard untuk memudahkan monitoring menyeluruh.
    - Sediakan pelatihan bagi staf akademik untuk membaca dan menindaklanjuti hasil dashboard secara efektif.

