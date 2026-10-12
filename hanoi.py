def menara_hanoi(n, tiang_asal, tiang_tujuan, tiang_bantu):
    # Base Case: jika tinggal 1 cakram, langsung pindahkan
    if n == 1:
        print(f"Pindahkan cakram 1 dari tiang {tiang_asal} ke tiang {tiang_tujuan}")
        return

    # 1. Pindahkan (n - 1) cakram dari asal ke bantu
    menara_hanoi(n - 1, tiang_asal, tiang_bantu, tiang_tujuan)

    # 2. Pindahkan cakram terbesar (ke-n) dari asal ke tujuan
    print(f"Pindahkan cakram {n} dari tiang {tiang_asal} ke tiang {tiang_tujuan}")

    # 3. Pindahkan (n - 1) cakram dari bantu ke tujuan
    menara_hanoi(n - 1, tiang_bantu, tiang_tujuan, tiang_asal)


if __name__ == "__main__":
    jumlah_cakram = 3
    print(f"Langkah-langkah menyelesaikan Menara Hanoi untuk {jumlah_cakram} cakram:")
    print("-" * 55)
    menara_hanoi(jumlah_cakram, 'A', 'C', 'B')
