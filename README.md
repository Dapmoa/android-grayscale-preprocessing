# Android Grayscale Dataset Preprocessing

Repository ini berisi script Python untuk melakukan prapemrosesan dataset aplikasi Android dengan mengubah file APK menjadi citra grayscale. Hasil konversi dapat digunakan sebagai dataset untuk penelitian atau pengembangan model Machine Learning.

---

## Struktur Repository

```
android-grayscale-preprocessing/
│
├── convertmal.py
├── convertbegn.py
├── README.md
```

---

# Persyaratan

Sebelum menjalankan script, pastikan telah tersedia:

- Virtual Machine REMnux
- Python 3
- 7-Zip (7z)
- Sampel APK Malware
- Sampel APK Benign

---

# Struktur Folder Kerja

```
Example/
│
├── zip malware/
│
├── Sampel Malware/
├── Sampel Benign/
│
├── Grayscale Malware/
├── Grayscale Benign/
│
├── convertmal.py
└── convertbegn.py
```

---

# Langkah 1 - Mengunduh Sampel Android

## Sampel Malware

1. Buka **MalwareBazaar**.
2. Cari sampel dengan tipe file **APK**.
3. Unduh sampel malware yang dibutuhkan.
4. Simpan seluruh file ZIP ke folder:

```
zip malware/
```

## Sampel Benign

1. Buka **F-Droid**.
2. Pilih aplikasi Android.
3. Unduh file APK.
4. Simpan sebagai sampel benign.

---

# Langkah 2 - Memindahkan File ke REMnux

Pindahkan seluruh file ke Virtual Machine REMnux menggunakan salah satu metode berikut:

- Shared Folder VirtualBox
- Drag and Drop
- SCP
- Flashdisk

Pada implementasi ini digunakan media **flashdisk**.

---

# Langkah 3 - Mengekstrak Sampel Malware

Jalankan perintah berikut pada Terminal REMnux.

```bash
for f in "./zip malware/"*.zip; do
    7z x "$f" -pinfected -o"./Sampel Malware"
done
```

Password yang digunakan:

```
infected
```

Hasil ekstraksi akan tersimpan pada folder:

```
Sampel Malware/
```

---

# Langkah 4 - Mengubah APK Menjadi Citra Grayscale

## Konversi Malware

```bash
python3 convertmal.py
```

## Konversi Benign

```bash
python3 convertbegn.py
```

> **Catatan**
>
> Lama proses konversi bergantung pada jumlah dan ukuran file APK.

---

# Langkah 5 - Hasil Konversi

Setelah proses selesai, hasil citra grayscale akan tersimpan pada folder:

```
Grayscale Malware/
Grayscale Benign/
```

---

# Langkah 6 - Memindahkan Hasil

Salin seluruh hasil konversi ke komputer server.

Pada implementasi ini digunakan media **flashdisk**.

---

# Catatan

Repository ini hanya berisi:

- Script Python
- Dokumentasi penggunaan

Repository **tidak menyertakan**:

- Sampel malware
- Sampel benign
- Dataset
- File APK

Pengguna dapat memperoleh sampel malware melalui **MalwareBazaar** dan sampel benign melalui **F-Droid** sesuai kebutuhan penelitian masing-masing.

---

## Author

**Daffa Maulana**

D3 Teknologi Komputer  
Telkom University
