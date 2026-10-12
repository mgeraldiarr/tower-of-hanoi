# Penyelesaian Algoritma Menara Hanoi (Tower of Hanoi)

## 1. Deskripsi Masalah
Tujuan dari permainan Menara Hanoi adalah memindahkan tumpukan $n$ cakram dari tiang asal (A) ke tiang tujuan (C) dengan bantuan tiang perantara (B), dengan aturan:
1. Hanya satu cakram yang dapat dipindahkan dalam satu waktu.
2. Cakram yang lebih besar tidak boleh berada di atas cakram yang lebih kecil.
3. Hanya cakram paling atas yang boleh diambil.

## 2. Pendekatan Solusi (Algoritma Rekursif)
Untuk memindahkan $n$ cakram dari tiang $A$ ke tiang $C$ menggunakan tiang $B$:
- **Langkah 1:** Pindahkan $(n-1)$ cakram dari tiang A ke tiang B menggunakan tiang C.
- **Langkah 2:** Pindahkan cakram ke-$n$ (cakram terbesar) langsung dari tiang A ke tiang C.
- **Langkah 3:** Pindahkan $(n-1)$ cakram dari tiang B ke tiang C menggunakan tiang A.

Rumus jumlah langkah minimum: 
Langkah = 2^n - 1
Untuk 3 cakram: 2^3 - 1 = 7 langkah.

## 3. Rincian 7 Langkah (3 Cakram)
1. Cakram 1 dipindahkan dari tiang A ke tiang C
2. Cakram 2 dipindahkan dari tiang A ke tiang B
3. Cakram 1 dipindahkan dari tiang C ke tiang B
4. Cakram 3 dipindahkan dari tiang A ke tiang C
5. Cakram 1 dipindahkan dari tiang B ke tiang A
6. Cakram 2 dipindahkan dari tiang B ke tiang C
7. Cakram 1 dipindahkan dari tiang A ke tiang C

## 4. Cara Menjalankan Program
Jalankan file kode menggunakan Python:
```bash
python hanoi.py
