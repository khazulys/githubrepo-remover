# Hapus Repositori GitHub

Sebuah skrip Python interaktif untuk menghapus beberapa repositori GitHub sekaligus dengan aman. Skrip ini mengambil semua repositori Anda, menampilkannya dalam daftar interaktif, dan memungkinkan Anda memilih mana yang akan dihapus.

## Fitur

- **Otentikasi Aman**: Menggunakan GitHub Personal Access Token (PAT) yang disimpan di environment variables.
- **Interaktif**: Menampilkan checklist semua repositori Anda untuk dipilih.
- **Aman**: Membutuhkan pilihan eksplisit dari pengguna, mengurangi risiko penghapusan yang tidak disengaja.
- **Bulk Delete**: Mampu menghapus beberapa repositori dalam satu kali eksekusi.

---

## ⚠️ Peringatan Keras

**Tindakan ini bersifat permanen dan tidak dapat diurungkan.** Repositori yang telah dihapus TIDAK BISA dikembalikan. Pastikan Anda benar-benar yakin sebelum menghapus. Gunakan dengan sangat hati-hati.

---

## Prasyarat

- Python 3.6+
- `pip` (Python package installer)

## Instalasi

1.  **Clone Repositori (jika belum)**
    ```bash
    # Gantilah dengan URL repositori yang benar jika Anda meng-clone dari remote
    # cd remove_repo 
    ```

2.  **Install dependensi Python yang dibutuhkan:**
    ```bash
    pip install requests python-dotenv InquirerPy
    ```

## Konfigurasi

Skrip ini memerlukan kredensial GitHub Anda untuk mengakses API.

1.  **Buat Personal Access Token (PAT)**
    - Buka halaman [Personal Access Tokens](https://github.com/settings/tokens) di pengaturan akun GitHub Anda.
    - Klik **"Generate new token"**.
    - Beri nama token, misalnya `RepoRemoverScript`.
    - Pada bagian **"Select scopes"**, centang scope `delete_repo`. Ini sangat penting agar skrip memiliki izin untuk menghapus repositori.
    - Klik **"Generate token"** di bagian bawah halaman.
    - **Salin token yang muncul.** Anda tidak akan bisa melihatnya lagi setelah meninggalkan halaman ini.

2.  **Buat File `.env`**
    - Di dalam direktori proyek ini, buat sebuah file baru bernama `.env`.
    - Buka file `.env` dan tambahkan baris berikut. Ganti `username-anda` dengan username GitHub Anda dan `token-yang-tadi-disalin` dengan PAT yang baru saja Anda buat.

    ```env
    GITHUB_USERNAME="username-anda"
    GITHUB_TOKEN="token-yang-tadi-disalin"
    ```

## Penggunaan

Setelah instalasi dan konfigurasi selesai, jalankan skrip dengan perintah:

```bash
python remove.py
```

- Skrip akan mengambil daftar repositori Anda.
- Gunakan tombol panah ▲/▼ untuk navigasi.
- Tekan `Spasi` untuk memilih atau membatalkan pilihan repositori.
- Tekan `Enter` untuk mengkonfirmasi pilihan Anda dan memulai proses penghapusan.