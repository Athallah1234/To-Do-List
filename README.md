# Aplikasi ToDo List yang Ditingkatkan

Aplikasi ToDo List ini ditulis menggunakan Python dan Tkinter. Aplikasi ini dirancang untuk membantu Anda mengelola tugas dengan cara yang efisien dan intuitif. Dengan antarmuka yang ramah pengguna, Anda dapat menambahkan, mengedit, menghapus, dan menandai tugas Anda dengan mudah.

## Fitur Utama

- **Tambahkan Tugas**: Masukkan tugas baru dengan prioritas yang dapat dipilih (Tinggi, Sedang, Rendah) dan tenggat waktu yang dapat ditentukan.
- **Hapus Tugas**: Hapus tugas yang telah selesai atau tidak diperlukan.
- **Edit Tugas**: Ubah deskripsi tugas yang sudah ada.
- **Tandai Tugas Selesai**: Tandai tugas yang telah selesai untuk menandakan kemajuan Anda.
- **Pencarian Tugas**: Cari tugas berdasarkan kata kunci.
- **Sortir Tugas**: Atur tugas berdasarkan prioritas.
- **Tenggat Waktu**: Tugas yang sudah melewati tenggat waktu akan ditandai dengan warna merah untuk menarik perhatian.
- **Bersihkan Semua Tugas**: Hapus semua tugas sekaligus jika diperlukan.

## Instalasi

Untuk menggunakan aplikasi ini, ikuti langkah-langkah berikut:

1. **Kloning Repositori**: Klon repositori ini ke mesin lokal Anda dengan perintah berikut:
    ```bash
    git clone https://github.com/username/repo.git
    ```
   Gantilah `username` dan `repo` dengan nama pengguna dan nama repositori Anda.

2. **Masuk ke Direktori Proyek**: 
    ```bash
    cd repo
    ```

3. **Jalankan Aplikasi**: 
    Pastikan Anda memiliki Python 3.x dan Tkinter yang sudah terpasang, kemudian jalankan aplikasi:
    ```bash
    python main.py
    ```

## Persyaratan

- Python 3.x
- Tkinter (biasanya sudah termasuk dalam instalasi Python)

## Penjelasan Kode

Aplikasi ini dibangun menggunakan struktur yang sederhana dan mudah dipahami. Berikut adalah penjelasan singkat tentang komponen utama dalam kode:

- **Import Library**: Aplikasi ini menggunakan `tkinter` untuk antarmuka pengguna, `datetime` untuk pengelolaan tanggal, dan `tkinter.font` untuk mengatur font.
  
- **Fungsi Utama**: 
  - `add_task()`: Menambahkan tugas baru dengan prioritas dan tenggat waktu.
  - `delete_task()`: Menghapus tugas yang dipilih dari daftar.
  - `clear_tasks()`: Menghapus semua tugas dalam daftar.
  - `edit_task()`: Mengedit tugas yang dipilih.
  - `mark_task_completed()`: Menandai tugas yang telah selesai.
  - `search_task()`: Mencari tugas berdasarkan kata kunci.
  - `check_overdue_tasks()`: Memeriksa dan menandai tugas yang telah melewati tenggat waktu.
  - `sort_tasks()`: Mengurutkan tugas berdasarkan prioritas.

- **Antarmuka Pengguna**: Aplikasi ini menggunakan `tkinter` untuk membangun antarmuka yang ramah pengguna, termasuk kolom input, dropdown untuk prioritas, dan tombol untuk melakukan berbagai fungsi.

## Masalah Umum dan Solusi

- **Masalah Menjalankan Aplikasi**: Jika Anda mengalami kesulitan saat menjalankan aplikasi, pastikan Python 3.x sudah terinstal dengan benar.
  
- **Tkinter Tidak Terinstal**: Jika Anda tidak dapat mengimpor Tkinter, instal dengan cara:
    ```bash
    sudo apt-get install python3-tk  # Untuk sistem Linux
    ```
  
- **Kesalahan Tanggal**: Jika Anda menerima pesan kesalahan terkait tanggal, pastikan Anda memasukkan tanggal dalam format `YYYY-MM-DD`.

## Lisensi

Aplikasi ini dirilis di bawah [Lisensi MIT](LICENSE). Anda bebas menggunakan, menyalin, memodifikasi, atau mendistribusikan aplikasi ini selama mencantumkan kredit kepada pengembang asli.

## Kontak

Jika Anda ingin menghubungi pengembang untuk memberikan umpan balik atau pertanyaan, silakan kirim email ke:
- [email@example.com](mailto:email@example.com)  <!-- Gantilah dengan alamat email Anda -->
