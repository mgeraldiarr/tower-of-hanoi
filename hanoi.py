def menara_hanoi(n, asal, tujuan, bantuan):
    # Base Case: jika hanya 1 piringan, pindahkan langsung
    if n == 1:
        print(f"Pindahkan piringan 1 dari tiang {asal} ke tiang {tujuan}")
        return

    # Langkah 1: Pindahkan n - 1 piringan dari asal ke tiang bantuan
    menara_hanoi(n - 1, asal, bantuan, tujuan)

    # Langkah 2: Pindahkan piringan ke-n (terbesar) dari asal ke tiang tujuan
    print(f"Pindahkan piringan {n} dari tiang {asal} ke tiang {tujuan}")

    # Langkah 3: Pindahkan n - 1 piringan dari tiang bantuan ke tiang tujuan
    menara_hanoi(n - 1, bantuan, tujuan, asal)


# Eksekusi untuk 3 piringan
jumlah_piringan = 3
menara_hanoi(jumlah_piringan, "A", "C", "B")
